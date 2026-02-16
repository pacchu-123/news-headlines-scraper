import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

with open("head_lines.txt", "w", encoding="utf-8") as f:
    for i, h in enumerate(headlines[:10], 1):
        f.write(f"{i}. {h.text.strip()}\n")

print("Headlines saved successfully!")
