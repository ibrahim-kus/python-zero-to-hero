
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

html_content = requests.get(url,headers=headers).content # or text # headers eklememizin sebebi tarayıcıyı taklit etmek tarayıcıdan göndermiş gibi davranmak.
soup = BeautifulSoup(html_content,"html.parser")

list = soup.find("ul", {"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 iyTDQy compact-list-view ipc-metadata-list--base"}).find_all("li", limit=100)

for item in list:
    filmName = item.find("h3", {"class":"ipc-title__text"}).text
    print(filmName)
#print(list)



