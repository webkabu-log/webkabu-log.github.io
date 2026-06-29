import os
import glob
import re
from bs4 import BeautifulSoup

site_dir = r"c:\trader"
sitemap_path = os.path.join(site_dir, "sitemap.xml")

import xml.etree.ElementTree as ET

# Parse sitemap to get dates
url_dates = {}
if os.path.exists(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    # xml namespace handling
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for url in root.findall('ns:url', ns):
        loc = url.find('ns:loc', ns)
        lastmod = url.find('ns:lastmod', ns)
        if loc is not None and lastmod is not None:
            filename = loc.text.strip().split("/")[-1]
            if not filename:
                filename = "index.html"
            url_dates[filename] = lastmod.text.strip()

# Default date
default_date = "2026-06-29"

# Pages to noindex
noindex_pages = [f"day{i}.html" for i in range(1, 9)] + ["hajimari.html"]

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    head = soup.find("head")
    if not head:
        return

    modified = False

    # Get date
    pub_date = url_dates.get(filename, default_date)
    jp_date = pub_date.replace("-", "/") # Simple format for display

    # Add noindex to thin pages
    if filename in noindex_pages:
        if not head.find("meta", attrs={"name": "robots"}):
            new_meta = soup.new_tag("meta", attrs={"name": "robots", "content": "noindex, follow"})
            head.append(new_meta)
            modified = True

    # Check if it's index.html
    if filename == "index.html":
        if not head.find("script", attrs={"type": "application/ld+json"}):
            schema = soup.new_tag("script", attrs={"type": "application/ld+json"})
            schema.string = f'''
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Web収益だけで株を買う日記",
      "url": "https://webkabu-log.github.io/"
    }}
    '''
            head.append(schema)
            modified = True

    # Check if it's an article page (has article-hero)
    article_hero = soup.find("header", class_=re.compile(r"article-hero"))
    is_info_page = filename in ["profile.html", "contact.html", "privacy.html", "monetization.html", "roadmap.html", "tools.html"]
    
    # Exclude redirect or stub pages
    if filename in ["job-log-09.html", "monthly-report-2026-06.html", "icon-preview.html", "icon-render.html"]:
        article_hero = None

    if article_hero and not is_info_page and filename != "index.html":
        # Add Article Schema
        if not head.find("script", attrs={"type": "application/ld+json"}):
            title_tag = soup.find("title")
            title = title_tag.text.split("|")[0].strip() if title_tag else ""
            desc_tag = head.find("meta", attrs={"name": "description"})
            desc = desc_tag["content"] if desc_tag and "content" in desc_tag.attrs else ""
            
            schema = soup.new_tag("script", attrs={"type": "application/ld+json"})
            schema.string = f'''
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{desc}",
      "author": {{
        "@type": "Person",
        "name": "ショウヤ",
        "url": "https://webkabu-log.github.io/profile.html"
      }},
      "datePublished": "{pub_date}",
      "dateModified": "{pub_date}"
    }}
    '''
            head.append(schema)
            modified = True

        # Add author meta tag
        if not head.find("meta", attrs={"name": "author"}):
            meta_author = soup.new_tag("meta", attrs={"name": "author", "content": "ショウヤ"})
            head.append(meta_author)
            modified = True

        # Add time element to article-hero
        if not article_hero.find("time"):
            time_wrapper = soup.new_tag("div", attrs={"class": "article-meta"})
            time_wrapper["style"] = "margin-bottom: 1.5rem; color: var(--text-muted); font-size: 0.9rem;"
            
            time_tag = soup.new_tag("time", attrs={"datetime": pub_date})
            time_tag.string = f"公開日: {jp_date}"
            
            author_span = soup.new_tag("span")
            author_span["style"] = "margin-left: 1rem;"
            author_span.string = "著者: "
            author_link = soup.new_tag("a", href="profile.html")
            author_link.string = "ショウヤ"
            author_span.append(author_link)
            
            time_wrapper.append(time_tag)
            time_wrapper.append(author_span)
            
            # Insert after the h1
            h1 = article_hero.find("h1")
            if h1:
                h1.insert_after(time_wrapper)
                modified = True
                
    if modified:
        # Use a formatter or just string dump
        html_out = str(soup)
        # BeautifulSoup can mess up some formatting, let's fix empty tags
        html_out = html_out.replace("></meta>", ">").replace("></link>", ">")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"Updated {filename}")

html_files = glob.glob(os.path.join(site_dir, "*.html"))
for f in html_files:
    process_file(f)

print("Done")
