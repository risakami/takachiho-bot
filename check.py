import requests
from bs4 import BeautifulSoup

url = “https://eipro.jp/takachiho1/eventCalendars/index”

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

if "残" in soup.text:
    print("残！")
