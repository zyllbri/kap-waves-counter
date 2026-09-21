import re
import requests

PROFILE_URL = "https://www.tradingview.com/u/Kap_Waves/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(PROFILE_URL, headers=headers, timeout=30)

print("Status:", response.status_code)
print("Page size:", len(response.text))

# Look for TradingView idea/chart URLs
patterns = [
    r'https://www\.tradingview\.com/chart/[A-Za-z0-9_]+/[A-Za-z0-9]+-[^"\\]+',
    r'/chart/[A-Za-z0-9_]+/[A-Za-z0-9]+-[^"\\]+',
]

found = set()

for pattern in patterns:
    matches = re.findall(pattern, response.text, re.IGNORECASE)

    for match in matches:
        if match.startswith("/"):
            match = "https://www.tradingview.com" + match

        found.add(match)

print("IDEAS FOUND:", len(found))

for url in sorted(found):
    print(url)
