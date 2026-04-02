import requests
from bs4 import BeautifulSoup

url ="https://eipro.jp/takachiho1/eventCalendars/index"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

if "残" in soup.text:
    print("残！")
else:
    print("なし")