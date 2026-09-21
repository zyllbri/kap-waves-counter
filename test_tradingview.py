import re
import requests

url = "https://www.tradingview.com/chart/ZIGUSD/2YCCIC4G-ZIGChain-ZIGUSD-The-Structure-Is-Starting-to-Resolve/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)
print("Page size:", len(response.text))

# Look for numbers near the eye/view indicator
patterns = [
    r'"views"\s*:\s*(\d+)',
    r'"viewCount"\s*:\s*(\d+)',
    r'"viewsCount"\s*:\s*(\d+)',
    r'"views_count"\s*:\s*(\d+)',
]

for pattern in patterns:
    match = re.search(pattern, response.text, re.IGNORECASE)

    if match:
        print("VIEW COUNT FOUND:", match.group(1))
        break
else:
    print("VIEW COUNT NOT FOUND")
