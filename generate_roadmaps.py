import os
import glob
from bs4 import BeautifulSoup

def generate_roadmap(filename, title, lead, articles_data, theme):
    # read roadmap.html as template
    with open('c:/trader/roadmap.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Update Title & Meta
    if soup.title:
        soup.title.string = f'{title} | Web収益だけで株を買う日記'
    
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc: meta_desc['content'] = lead
    
    meta_og_title = soup.find('meta', {'property': 'og:title'})
    if meta_og_title: meta_og_title['content'] = title
    
    meta_og_desc = soup.find('meta', {'property': 'og:description'})
    if meta_og_desc: meta_og_desc['content'] = lead
    
    meta_og_url = soup.find('meta', {'property': 'og:url'})
    if meta_og_url: meta_og_url['content'] = f'https://webkabu-log.github.io/{filename}'

    # Update Hero
    hero = soup.find('header', class_='atlas-hero')
    if hero:
        hero.find('p', class_='atlas-hero-eyebrow').string = f'{theme.upper()} ATLAS'
        hero.find('h1').string = title
        hero.find('p', class_='atlas-hero-lead').string = lead
        
        hero_stats = hero.find_all('strong')
        if len(hero_stats) >= 3:
            hero_stats[0].string = f'公開記事数: {len(articles_data)}'
            hero_stats[1].string = f'AI活用ログ' if 'AI' in title else '就活記録'
            hero_stats[2].string = '経験を言葉にする'

    # Clear nav list and chapters
    nav_list = soup.find('ul', class_='atlas-nav-list')
    if nav_list: nav_list.clear()

    main_div = soup.find('main').find('div', class_='atlas-container')
    chapters = main_div.find_all('section', class_='atlas-chapter')
    for c in chapters:
        c.decompose()

    chapter_html = f'''
    <section class="atlas-chapter is-last" id="chapter-1">
      <div class="atlas-chapter-bg-num" aria-hidden="true">01</div>
      <div class="atlas-chapter-header atlas-reveal">
        <div class="atlas-chapter-title-wrap">
          <h2>{title} の軌跡</h2>
        </div>
        <p class="atlas-chapter-desc">これまでの全記録です。（記事数: {len(articles_data)}）</p>
      </div>
      <div class="atlas-timeline-container">
        <div class="atlas-timeline-line"></div>
        <svg class="atlas-timeline-svg" viewBox="0 0 100 1000" preserveAspectRatio="none" aria-hidden="true" focusable="false">
          <path class="atlas-timeline-path-bg" d="M 50,0 L 50,1000" vector-effect="non-scaling-stroke" />
          <path class="atlas-timeline-path" d="M 50,0 L 50,1000" vector-effect="non-scaling-stroke" />
        </svg>
        <ol class="atlas-timeline-list">
    '''
    
    for i, a in enumerate(articles_data):
        is_latest = 'is-latest' if i == len(articles_data)-1 else ''
        tag = '<span class="atlas-status-tag is-latest">最新公開</span>' if is_latest else '<span class="atlas-status-tag">公開済み</span>'
        chapter_html += f'''
          <li class="atlas-timeline-item is-published {is_latest} atlas-reveal">
            <article class="atlas-card {is_latest}">
              <div class="atlas-card-meta">
                <span class="study-num">Log {i+1:02d}</span>
                {tag}
              </div>
              <h3>{a['title']}</h3>
              <a class="atlas-card-link" href="{a['href']}">読む</a>
            </article>
          </li>
        '''
        
    chapter_html += '''
        </ol>
      </div>
    </section>
    '''
    
    new_chapter_soup = BeautifulSoup(chapter_html, 'html.parser')
    main_div.find('article').append(new_chapter_soup)
    
    with open(f'c:/trader/{filename}', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f'Generated {filename}')

def get_title(path):
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        h1 = soup.find('h1')
        return h1.text if h1 else os.path.basename(path)

ai_tips_files = sorted(glob.glob('c:/trader/ai-tips-*.html'))
job_log_files = sorted(glob.glob('c:/trader/job-log-*.html')) + sorted(glob.glob('c:/trader/study-ai-jobhunting-*.html'))

ai_tips_data = [{'href': os.path.basename(f), 'title': get_title(f)} for f in ai_tips_files]
job_log_data = [{'href': os.path.basename(f), 'title': get_title(f)} for f in job_log_files]

generate_roadmap('ai-tips-roadmap.html', 'AI活用ロードマップ', 'ブログ執筆や情報整理にAIを活用する記録です。', ai_tips_data, 'AI TIPS')
generate_roadmap('job-log-roadmap.html', 'AI就活ロードマップ', '自己分析やES作成などの就活準備にAIを活用する記録です。', job_log_data, 'JOB LOG')
