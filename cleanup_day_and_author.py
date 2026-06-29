import os
import re

target_dir = r"c:\trader"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Task 2: Unify author name "ショウヤ" -> "ショウ"
    content = content.replace("ショウヤ", "ショウ")

    # Task 1: Hide "day" logs and related links

    # 1. Remove the entire day-records section in index.html
    content = re.sub(
        r'<section[^>]*id="day-records"[^>]*>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Remove nav links and buttons pointing to index.html#day-records
    content = re.sub(
        r'\s*<a[^>]*href="index\.html#day-records"[^>]*>.*?</a>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # 3. Remove article navigation blocks (Next/Prev) to day pages
    content = re.sub(
        r'\s*<a[^>]*class="[^"]*article-nav-(prev|next)[^"]*"[^>]*href="(day\d+|hajimari)\.html"[^>]*>.*?</a>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # 4. Remove button links (e.g., secondary-button, read-button) to day pages
    content = re.sub(
        r'\s*<a[^>]*class="[^"]*button[^"]*"[^>]*href="(day\d+|hajimari)\.html"[^>]*>.*?</a>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # 5. Remove any list items containing links to day pages
    content = re.sub(
        r'\s*<li>\s*<a[^>]*href="(day\d+|hajimari)\.html"[^>]*>.*?</a>\s*</li>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    # 6. Fallback: Any other links to dayX.html or hajimari.html
    content = re.sub(
        r'\s*<a[^>]*href="(day\d+|hajimari)\.html"[^>]*>.*?</a>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("Operation complete.")
