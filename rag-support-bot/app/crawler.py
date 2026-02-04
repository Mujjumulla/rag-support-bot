import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_website(start_url, max_pages=20):
    visited = set()
    to_visit = [start_url]
    results = []

    domain = urlparse(start_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            text = soup.get_text(separator=" ", strip=True)
            results.append({"url": url, "text": text})

            visited.add(url)

            for link in soup.find_all("a", href=True):
                next_url = urljoin(url, link["href"])
                if urlparse(next_url).netloc == domain:
                    if next_url not in visited:
                        to_visit.append(next_url)

        except Exception:
            continue

    return results
