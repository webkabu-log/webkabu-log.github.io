import os
import glob
import re
from bs4 import BeautifulSoup

site_dir = "c:/trader"

# 1. Update styles.css
css_path = os.path.join(site_dir, 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# I will find the block starting with "/* Series Nav Panel */" and replace the relevant parts.
# Let's use a simpler approach: I'll replace the exact strings.

new_series_dot = """
.series-dot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 22px;
  background: var(--paper);
  border: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.3s ease;
}

.series-dot:hover {
  border-color: var(--green);
  color: var(--green);
  transform: translateY(-2px);
}

.series-dot.is-current {
  background: var(--green);
  color: white;
  border-color: var(--green);
  font-weight: bold;
  padding: 0 16px;
  width: auto;
}

.series-dot.is-current::after {
  content: "現在地";
  font-size: 0.75rem;
  margin-left: 6px;
  opacity: 0.9;
  font-weight: normal;
}
"""

new_summary_card = """
/* Summary Card */
.summary-card {
  background: var(--panel);
  border-left: 4px solid var(--green);
  border-radius: 8px;
  padding: 24px;
  margin: 30px 0;
  box-shadow: 0 4px 15px rgba(28, 37, 33, 0.05);
  position: relative;
  transition: all 0.3s ease;
}

.summary-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(28, 37, 33, 0.08);
}

.summary-card h2 {
  margin-top: 0 !important;
  font-size: 1.3rem !important;
  color: var(--ink);
  border-bottom: 1px solid var(--line);
  padding-bottom: 12px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.summary-card h2::before {
  content: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="%231b7a5b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>');
  display: inline-block;
  width: 24px;
  height: 24px;
  margin-right: 4px;
}
"""

# Apply the replacements using regex to safely replace the blocks
css_content = re.sub(
    r'\.series-dot\s*\{.*?(?=\/\* Summary Card \*\/)',
    new_series_dot + '\n',
    css_content,
    flags=re.DOTALL
)

css_content = re.sub(
    r'\/\* Summary Card \*\/\s*\.summary-card\s*\{.*?(?=$)',
    new_summary_card,
    css_content,
    flags=re.DOTALL
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated styles.css")

# 2. Update Global Nav and Series Nav Titles in all HTML files
html_files = glob.glob(os.path.join(site_dir, '*.html'))
for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the duplicate Roadmap link if exists
    # Currently it is: <a href="roadmap.html">投資学習</a>\n<a href="roadmap.html">ロードマップ</a>
    html = re.sub(r'<a href="roadmap\.html">ロードマップ</a>\s*', '', html)
    
    # Fix the title attribute of series dots. Wait, in HTML it's <a ... title="Study XX">
    # Let's use BeautifulSoup for safer replacement of the series-dot titles
    soup = BeautifulSoup(html, 'html.parser')
    
    dots = soup.find_all('a', class_='series-dot')
    if dots:
        prefix_name = "Study"
        if filename.startswith('ai-tips'):
            prefix_name = "AI活用"
        elif filename.startswith('job-log') or filename.startswith('study-ai-jobhunting'):
            prefix_name = "AI就活"
        
        for dot in dots:
            title_attr = dot.get('title', '')
            if 'Study' in title_attr and prefix_name != "Study":
                dot['title'] = title_attr.replace('Study', prefix_name)

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
print("Updated HTML files for Nav and Dots")

# 3. Clean up the AI Roadmaps (remove the glossary and official links)
roadmaps_to_clean = ['ai-tips-roadmap.html', 'job-log-roadmap.html']
for rm in roadmaps_to_clean:
    rm_path = os.path.join(site_dir, rm)
    if os.path.exists(rm_path):
        with open(rm_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        container = soup.find('div', class_='atlas-container')
        if container:
            article = container.find('article')
            if article:
                chapter_1 = article.find('section', id='chapter-1')
                if chapter_1:
                    article.clear()
                    article.append(chapter_1)
        
        with open(rm_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
print("Cleaned up AI roadmaps.")
