import requests
from bs4 import BeautifulSoup

q = input("Enter your search query: ")

url = "https://duckduckgo.com/html/?q=" + q

headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find_all("a", class_="result__a")

for i, x in enumerate(results[:10], 1):
    print(i, x.get_text())
