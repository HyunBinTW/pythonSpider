import requests
from bs4 import BeautifulSoup

### Momo ###
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

url = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10194430&mdiv=1000700000-today-top13'
r = requests.get(url, headers = headers)
response = r.text
soup = BeautifulSoup(r.text,"html.parser")

#配送方式
deliveryMethod = soup.find('dl', class_='shippingList').find('dd').find('label')
deliveryText = deliveryMethod.text.strip();
print('配送方式 :' + deliveryText);

#商品特色
product = soup.find('ul', id='categoryActivityInfo').find_all('li')
productText = ''
for tag in product:
  # 輸出超連結的文字
  productText = productText + tag.text

print('商品特色 :' + productText);

#商品照片網址
productUrl = soup.find('div', id='goodsimg').find('a', href=True)
print('商品照片網址 :' + productUrl.get('href'));


### Yahoo  ###

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

yahoo_url = 'https://tw.mall.yahoo.com/item/%E4%B9%99-%E6%9B%BC%E7%A7%80%E9%9B%B7%E6%95%A6-35g%E3%80%90%E5%B1%88%E8%87%A3%E6%B0%8F%E3%80%91-p033088522660'
r = requests.get(yahoo_url, headers = headers)
response = r.text
soup = BeautifulSoup(r.text,"html.parser")


#配送方式
deliveryMethod = soup.prettify();
print(deliveryMethod)
deliveryText = deliveryMethod.text.strip();
print('配送方式 :' + deliveryText);

#商品特色
product = soup.find('ul', id='categoryActivityInfo').find_all('li')
productText = ''
for tag in product:
  # 輸出超連結的文字
  productText = productText + tag.text

print('商品特色 :' + productText);

#商品照片網址
productUrl = soup.find('div', id='goodsimg').find('a', href=True)
print('商品照片網址 :' + productUrl.get('href'));
