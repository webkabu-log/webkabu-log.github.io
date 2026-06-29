import os
import glob
import re
from bs4 import BeautifulSoup

site_dir = r"c:\trader"
img_dir = os.path.join(site_dir, "images", "eyecatch")

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

def chunk_string(s, length):
    return [s[0+i:length+i] for i in range(0, len(s), length)]

def generate_svg(filename, title):
    # Determine category
    bg_color = "#f8f9fa"
    emoji = "📝"
    
    if "study-investing" in filename:
        bg_color = "#e6f2ff"
        emoji = "📈"
    elif "ai-tips" in filename:
        bg_color = "#f3e8ff"
        emoji = "🤖"
    elif "job-log" in filename or "study-ai-jobhunting" in filename:
        bg_color = "#e6fffa"
        emoji = "💼"
    elif "day" in filename or "hajimari" in filename:
        bg_color = "#fff0f5"
        emoji = "📝"

    # Chunk title to max 15 characters per line
    lines = chunk_string(title, 15)
    if len(lines) > 3:
        lines = lines[:3]
        lines[-1] = lines[-1][:-1] + "..."

    svg_width = 1200
    svg_height = 630
    
    # Calculate Y coordinates for text to stay centered
    if len(lines) == 1:
        y_starts = [440]
    elif len(lines) == 2:
        y_starts = [400, 480]
    else:
        y_starts = [380, 460, 540]

    text_spans = ""
    for i, line in enumerate(lines):
        text_spans += f'<tspan x="600" y="{y_starts[i]}">{line}</tspan>'

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
    <rect width="100%" height="100%" fill="{bg_color}" rx="20"/>
    
    <text x="600" y="240" font-size="160px" text-anchor="middle" dominant-baseline="middle">{emoji}</text>
    
    <text font-family="sans-serif" font-weight="bold" font-size="56px" fill="#333333" text-anchor="middle">
        {text_spans}
    </text>
</svg>'''
    
    svg_filename = filename.replace(".html", ".svg")
    svg_path = os.path.join(img_dir, svg_filename)
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    return f"images/eyecatch/{svg_filename}"

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    
    article_hero = soup.find("header", class_=re.compile(r"article-hero"))
    is_info_page = filename in ["profile.html", "contact.html", "privacy.html", "monetization.html", "roadmap.html", "tools.html"]
    
    if filename in ["job-log-09.html", "monthly-report-2026-06.html", "icon-preview.html", "icon-render.html", "index.html"]:
        article_hero = None

    if article_hero and not is_info_page:
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
            # Re-generate SVG (this will overwrite existing ones)
            generate_svg(filename, title)
            print(f"Regenerated SVG for {filename}")

html_files = glob.glob(os.path.join(site_dir, "*.html"))
for f in html_files:
    process_file(f)

print("Done regenerating SVGs.")
