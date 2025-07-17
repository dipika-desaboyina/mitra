import requests
from bs4 import BeautifulSoup

# A simple bs4 based scraper that takes the Income Tax portal urls and converts them into markdown corpora while preserving their 
# structure and the information including demonstrative screenshots(preserved as hyperlinked urls in the markdown corpora).

TARGET_URL = "https://www.incometax.gov.in/iec/foportal/help/how-to-file-itr1-form-sahaj"
BASE_URL = "https://www.incometax.gov.in"
file_name = TARGET_URL.rsplit('/', 1)[-1]
OUTPUT_FILE = f"scraped_{file_name}.md"

def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.text

def table_to_markdown(table):
    rows = table.find_all('tr')
    if not rows:
        return ""
    
    header = [th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]
    md = ["| " + " | ".join(header) + " |", "| " + " | ".join(['---'] * len(header)) + " |"]

    for row in rows[1:]:
        cols = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
        md.append("| " + " | ".join(cols) + " |")

    return "\n".join(md)

def tag_to_md(tag):
    if tag.name in ['h1', 'h2', 'h3', 'h4']:
        level = int(tag.name[1])
        return f"{'#' * level} {tag.get_text(strip=True)}"
    elif tag.name == 'p':
        return tag.get_text(strip=True)
    elif tag.name == 'img':
        src = tag.get('src', '')
        if not src.startswith('http'):
            src = BASE_URL + src
        alt = tag.get('alt', '')
        return f"[{alt}]({src})"
    elif tag.name == 'ul':
        return '\n'.join([f"- {li.get_text(strip=True)}" for li in tag.find_all('li')])
    elif tag.name == 'ol':
        return '\n'.join([f"{i+1}. {li.get_text(strip=True)}" for i, li in enumerate(tag.find_all('li'))])
    elif tag.name == 'table':
        return table_to_markdown(tag)
    else:
        return ''

def find_main_content(soup):
    # Try known containers first
    for tag in ['main', 'article', 'section', 'div']:
        candidates = soup.find_all(tag)
        if candidates:
            largest = max(candidates, key=lambda el: len(el.get_text(strip=True)))
            if len(largest.get_text(strip=True)) > 200:
                return largest
    return soup.body

def extract_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = find_main_content(soup)
    lines = []

    for tag in content.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'img', 'ul', 'ol', 'table'], recursive=True):
        md = tag_to_md(tag)
        if md:
            lines.append(md.strip())

    return '\n\n'.join(lines)

def main():
    html = fetch_html(TARGET_URL)
    markdown = extract_markdown(html)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Markdown saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
