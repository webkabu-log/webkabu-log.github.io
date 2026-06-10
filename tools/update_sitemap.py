import os
import glob
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://webkabu-log.github.io/"

def update_sitemap():
    # C:\trader 直下のすべてのhtmlファイルを取得
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    urls = []

    for file_path in html_files:
        filename = os.path.basename(file_path)
        # Googleのサーチコンソール確認用ファイルや、テンポラリ・除外ファイルをスキップ
        if filename.startswith("google") or filename.startswith("temp_") or filename.startswith("test_"):
            continue

        with open(file_path, "r", encoding="utf-8", errors="ignore") as html_file:
            html = html_file.read()
        if re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*noindex', html, re.IGNORECASE):
            continue

        # 最終更新日時（YYYY-MM-DD）を取得
        mtime = os.path.getmtime(file_path)
        lastmod = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

        # トップページはURL末尾に index.html を付けない
        if filename == "index.html":
            loc = SITE_URL
        else:
            loc = f"{SITE_URL}{filename}"

        urls.append((loc, lastmod))

    # 表示順の整理: index.htmlを最上位にし、他はアルファベット順
    urls.sort(key=lambda x: (x[0] != SITE_URL, x[0]))

    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    
    # XMLの書き出し
    with open(sitemap_path, "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for loc, lastmod in urls:
            f.write('  <url>\n')
            f.write(f'    <loc>{loc}</loc>\n')
            f.write(f'    <lastmod>{lastmod}</lastmod>\n')
            f.write('  </url>\n')
        f.write('</urlset>\n')
        
    print(f"[SUCCESS] sitemap.xml has been updated with {len(urls)} URLs.")

if __name__ == "__main__":
    update_sitemap()
