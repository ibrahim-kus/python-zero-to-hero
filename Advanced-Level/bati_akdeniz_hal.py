import requests
from bs4 import BeautifulSoup


url = "https://www.batiakdeniztv.com/serik-hal-fiyatlari"

headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

html = requests.get(url,headers=headers).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("table", {"align":"center", "cellpadding":"13"})
#list = soup.find_all('table', align="center", cellpadding="13") second way

for table in list:
    unit = table.tbody.tr.td.text
    print(unit)
