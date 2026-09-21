import re
import requests
from urllib.parse import urljoin

SEARCH_URL = "https://www.tradingview.com/ideas/search/?query=Kap_Waves"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(SEARCH_URL, headers=headers, timeout=30)

print("Status:", response.status_code)
print("Page size:", len(response.text))

# Find TradingView idea/chart links
patterns = [
    r'href=["\'](/chart/[^"\']+)["\']',
    r'href=["\'](https://www\.tradingview\.com/chart/[^"\']+)["\']',
]

found = set()

for pattern in patterns:
    matches = re.findall(pattern, response.text, re.IGNORECASE)

    for match in matches:
        url = urljoin("https://www.tradingview.com", match)
        found.add(url)

print("IDEAS FOUND:", len(found))

for url in sorted(found):
    print(url)
