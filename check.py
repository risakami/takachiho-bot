import requests
from bs4 import BeautifulSoup
import os

url = "https://eipro.jp/takachiho1/eventCalendars/index"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

if "残1艇" in soup.text:
    webhook = os.environ["DISCORD_WEBHOOK"]
    requests.post(webhook, json={"content": "高千穂ボート空き出た！"})
    print("通知送信")
else:
    print("空きなし")