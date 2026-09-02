import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_trending_repos():
    url = "https://github.com/trending"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch trending page: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    repos = []
    
    articles = soup.find_all("article", class_="Box-row")
    
    for article in articles:
        try:
            h2 = article.find("h2")
            if not h2:
                continue
            a_tag = h2.find("a")
            if not a_tag:
                continue
            full_name = a_tag.get_text(strip=True).replace("\n", "").replace(" ", "")
            
            desc_tag = article.find("p", class_="color-fg-muted")
            description = desc_tag.get_text(strip=True) if desc_tag else "No description"
            
            lang_tag = article.find("span", itemprop="programmingLanguage")
            language = lang_tag.get_text(strip=True) if lang_tag else "N/A"
            
            star_link = article.find("a", class_="Link--muted")
            if star_link and star_link.find("svg", class_="octicon-star"):
                star_text = star_link.get_text(strip=True)
                star_count = star_text.replace(",", "").strip()
            else:
                star_count = "0"
            
            repos.append({
                "name": full_name,
                "description": description,
                "language": language,
                "stars": star_count,
                "url": f"https://github.com/{full_name}"
            })
        except Exception as e:
            print(f"Skipping a repo due to error: {e}")
            continue
    
    return repos

def generate_markdown(repos):
    today = datetime.now().strftime("%Y-%m-%d")
    md_lines = [
        f"# GitHub Trending - {today}",
        "",
        "| Rank | Repository | Description | Language | Stars Today |",
        "|------|------------|-------------|----------|-------------|"
    ]
    
    for idx, repo in enumerate(repos, 1):
        md_lines.append(
            f"| {idx} | [{repo['name']}]({repo['url']}) | {repo['description'][:50]} | {repo['language']} | {repo['stars']} |"
        )
    
    return "\n".join(md_lines)

def main():
    repos = get_trending_repos()
    if not repos:
        print("No repos found. Exiting.")
        return
    
    content = generate_markdown(repos)
    os.makedirs("trending", exist_ok=True)
    
    filename = f"trending/{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Successfully saved {len(repos)} trending repos to {filename}")

if __name__ == "__main__":
    main()
