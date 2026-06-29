import os
import glob
import re
from bs4 import BeautifulSoup

site_dir = r"c:\trader"

css_addition = """
/* =========================================
   Rich UI Enhancements (Series Nav & Summary Card)
========================================= */

/* Series Nav Panel */
.series-nav-panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 20px;
  margin: 30px 0;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
}

.series-nav-header {
  font-weight: bold;
  font-size: 1.1rem;
  margin-bottom: 12px;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 8px;
}

.series-nav-dots {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.series-dot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--bg-main);
  border: 1px solid var(--line);
  color: var(--text-muted);
  font-size: 0.8rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.series-dot:hover {
  border-color: var(--primary);
  color: var(--primary);
}

.series-dot.is-current {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
  font-weight: bold;
}

/* Summary Card */
.summary-card {
  background: linear-gradient(145deg, #ffffff, #f8f9fa);
  border-left: 4px solid var(--primary);
  border-radius: 8px;
  padding: 24px;
  margin: 30px 0;
  box-shadow: 0 8px 25px rgba(0,0,0,0.05);
  position: relative;
}

.summary-card::before {
  content: '✅';
  position: absolute;
  top: -12px;
  right: -12px;
  font-size: 24px;
  background: white;
  border-radius: 50%;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.summary-card h2 {
  margin-top: 0 !important;
  font-size: 1.3rem !important;
  color: var(--text-main);
  border-bottom: 1px solid var(--line);
  padding-bottom: 12px;
  margin-bottom: 16px;
}
"""

print("Skipping CSS append because it was already added.")

html_files = glob.glob(os.path.join(site_dir, '*.html'))

def get_series_data(prefix):
    files = sorted(glob.glob(os.path.join(site_dir, f'{prefix}*.html')))
    if prefix == 'job-log':
        files += sorted(glob.glob(os.path.join(site_dir, 'study-ai-jobhunting-*.html')))
    return [os.path.basename(f) for f in files]

series_map = {
    'ai-tips': ('AI活用', get_series_data('ai-tips'), '🤖'),
    'job-log': ('AI就活', get_series_data('job-log'), '💼'),
    'study-ai-jobhunting': ('AI就活', get_series_data('job-log'), '💼'),
    'study-investing': ('投資学習', get_series_data('study-investing'), '📈')
}

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Global Navigation Links
    html = html.replace('href="index.html#ai-tips"', 'href="ai-tips-roadmap.html"')
    html = html.replace('href="index.html#ai-records"', 'href="job-log-roadmap.html"')
    html = html.replace('href="index.html#study-notes"', 'href="roadmap.html"') # Keep investing as roadmap.html

    soup = BeautifulSoup(html, 'html.parser')
    
    # Process Article Pages for Series Nav and Summary Card
    article_body = soup.find('div', class_='article-body')
    if article_body:
        # Determine Series
        current_series = None
        for prefix, (name, files, icon) in series_map.items():
            if filename.startswith(prefix) and filename in files:
                current_series = (name, files, icon)
                break
        
        if current_series:
            name, files, icon = current_series
            # Build Series Nav if not exists
            if not soup.find('div', class_='series-nav-panel'):
                nav_html = f'''
                <div class="series-nav-panel reveal">
                  <div class="series-nav-header">{icon} {name}シリーズ ({len(files)}記事)</div>
                  <div class="series-nav-dots">
                '''
                for i, f in enumerate(files):
                    is_current = 'is-current' if f == filename else ''
                    nav_html += f'<a href="{f}" class="series-dot {is_current}" title="Study {i+1:02d}">{i+1}</a>'
                nav_html += '</div></div>'
                
                nav_soup = BeautifulSoup(nav_html, 'html.parser')
                article_body.insert(0, nav_soup)

        # Build Summary Card
        # Find <h2>今回わかったこと</h2> or similar
        h2s = article_body.find_all('h2')
        summary_h2 = None
        for h2 in h2s:
            if '今回わかったこと' in h2.text or 'わかったこと' in h2.text:
                summary_h2 = h2
                break
        
        if summary_h2 and (not summary_h2.parent.has_attr('class') or 'summary-card' not in summary_h2.parent.get('class', [])):
            # Gather all siblings until the next h2 or end
            siblings_to_wrap = [summary_h2]
            nxt = summary_h2.find_next_sibling()
            while nxt and nxt.name != 'h2' and 'next-links' not in nxt.get('class', []):
                siblings_to_wrap.append(nxt)
                nxt = nxt.find_next_sibling()
                
            wrapper = soup.new_tag('div', **{'class': 'summary-card reveal'})
            summary_h2.insert_before(wrapper)
            for el in siblings_to_wrap:
                wrapper.append(el)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Successfully enriched all articles.")
