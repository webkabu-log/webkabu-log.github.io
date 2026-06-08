import os
import glob
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class HTMLAnalyzer(HTMLParser):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.title = None
        self.meta_description = None
        self.h1_count = 0
        self.headings = []  # list of (tag, text)
        self.images = []    # list of (src, alt_exists, alt_value)
        self.links = []     # list of (href, line_number)
        self.ids = set()    # elements with id
        
        self._in_title = False
        self._current_heading_tag = None
        self._current_heading_text = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # IDの収集
        if "id" in attrs_dict:
            self.ids.add(attrs_dict["id"])
        if "name" in attrs_dict and tag == "a":
            self.ids.add(attrs_dict["name"])

        # タイトルの追従
        if tag == "title":
            self._in_title = True
            
        # メタ記述の取得
        elif tag == "meta":
            if attrs_dict.get("name") == "description":
                self.meta_description = attrs_dict.get("content", "").strip()
                
        # 見出しの取得
        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            if tag == "h1":
                self.h1_count += 1
            self._current_heading_tag = tag
            self._current_heading_text = []
            
        # 画像のアクセシビリティチェック
        elif tag == "img":
            src = attrs_dict.get("src", "")
            alt_exists = "alt" in attrs_dict
            alt_value = attrs_dict.get("alt", "")
            self.images.append((src, alt_exists, alt_value))
            
        # リンクの収集
        elif tag == "a":
            href = attrs_dict.get("href", "")
            line_no = self.getpos()[0]
            self.links.append((href, line_no))

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
        if self._current_heading_tag:
            self._current_heading_text.append(data)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            if self._current_heading_tag == tag:
                heading_text = "".join(self._current_heading_text).strip()
                self.headings.append((tag, heading_text))
                self._current_heading_tag = None

def check_website():
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    # Google確認用ファイルは除外
    html_files = [f for f in html_files if not os.path.basename(f).startswith("google")]

    analyzers = {}
    total_errors = 0
    total_warnings = 0

    print("===================================================")
    # 1. 各ファイルのパース
    for file_path in html_files:
        filename = os.path.basename(file_path)
        analyzer = HTMLAnalyzer(file_path)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            analyzer.feed(f.read())
        analyzers[filename] = analyzer

    # 2. 各ファイルの静的検証
    for filename, analyzer in sorted(analyzers.items()):
        print(f"\nAnalyzing: {filename}")
        print("-" * len(filename) * 2)
        errors = []
        warnings = []

        # --- SEOの検証 ---
        if not analyzer.title:
            errors.append("[SEO] Title tag is missing")
        elif len(analyzer.title.strip()) < 5:
            warnings.append(f"[SEO] Title is too short: '{analyzer.title}'")

        if not analyzer.meta_description:
            warnings.append("[SEO] Meta description is missing")
        elif len(analyzer.meta_description) < 20:
            warnings.append(f"[SEO] Meta description is very short: '{analyzer.meta_description}'")

        if analyzer.h1_count == 0:
            errors.append("[SEO] <h1> tag is missing")
        elif analyzer.h1_count > 1:
            errors.append(f"[SEO] Multiple <h1> tags found ({analyzer.h1_count} h1 tags)")

        # --- アクセシビリティの検証 ---
        # 画像のaltチェック
        for src, alt_exists, alt_value in analyzer.images:
            if not alt_exists:
                errors.append(f"[A11y] Image missing alt attribute: src='{src}'")
            elif not alt_value.strip():
                warnings.append(f"[A11y] Image has empty alt attribute (acceptable for decorative images, but check): src='{src}'")

        # 見出し構造の順番チェック
        prev_level = 0
        for tag, text in analyzer.headings:
            level = int(tag[1])
            if prev_level > 0 and (level - prev_level > 1):
                warnings.append(f"[A11y] Heading levels skipped: H{prev_level} to H{level} ('{text}')")
            prev_level = level

        # --- リンク切れチェック (同一サイト内) ---
        for href, line_no in analyzer.links:
            href_clean = href.strip()
            if not href_clean:
                warnings.append(f"[HTML] Empty link href on line {line_no}")
                continue

            # 外部URLや特殊なプロトコルは検証をスキップ
            if href_clean.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
                continue

            # アンカーリンクとパスの分解
            parsed = urlparse(href_clean)
            path = unquote(parsed.path)
            fragment = unquote(parsed.fragment)

            # 同一ファイル内アンカーリンクの検証
            if not path:
                if fragment and fragment not in analyzer.ids:
                    errors.append(f"[Link] Broken internal anchor link: '{href_clean}' on line {line_no} (ID '{fragment}' does not exist in this page)")
            else:
                # 相対パスの解決
                target_file = path
                if target_file not in analyzers:
                    # 実際のファイルシステムに存在するかチェック
                    full_target_path = os.path.normpath(os.path.join(BASE_DIR, target_file))
                    if not os.path.exists(full_target_path):
                        errors.append(f"[Link] Broken link to file: '{href_clean}' on line {line_no} (File '{target_file}' not found)")
                else:
                    # 対象ファイル内のアンカーリンクの検証
                    if fragment and fragment not in analyzers[target_file].ids:
                        errors.append(f"[Link] Broken anchor link: '{href_clean}' on line {line_no} (ID '{fragment}' does not exist in target page '{target_file}')")

        # 結果の出力
        for err in errors:
            print(f"  [ERROR] {err}")
        for warn in warnings:
            print(f"  [WARN]  {warn}")

        if not errors and not warnings:
            print("  [OK] No errors or warnings found.")

        total_errors += len(errors)
        total_warnings += len(warnings)

    print("\n===================================================")
    print(f"Validation Completed. Total Errors: {total_errors}, Total Warnings: {total_warnings}")
    print("===================================================")

    if total_errors > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(check_website())
