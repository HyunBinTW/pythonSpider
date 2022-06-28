import requests
from bs4 import BeautifulSoup

# Momo
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

url = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10194430&mdiv=1000700000-today-top13'
r = requests.get(url, headers = headers)
response = r.text
soup = BeautifulSoup(r.text,"html.parser")

print(soup)



# Yahoo