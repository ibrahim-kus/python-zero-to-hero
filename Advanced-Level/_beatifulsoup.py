#Scraping library

from bs4 import BeautifulSoup

html_doc = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First index page</title>
</head>
<body>
    python course
    <h1>h1 text </h1>
    <h2>h2 text 111</h2>
    <h2>h2 text 222</h2>
    <div> <h1>div h1 text </h1>
    <h2>div h2 text 111</h2>
    <h2>div h2 text 222</h2> </div>
    <div>
    <ul>
    <li>li1</li>
    <li>li2</li>
    </ul></div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string
result = soup.h1

result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('div')[1].ul.find_all('li')
result = soup.div.findChildren()
result = soup.div.findNextSibling() 


print(result)