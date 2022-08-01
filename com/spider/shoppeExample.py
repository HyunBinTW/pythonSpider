# headless 瀏覽器 = 無介面板的瀏覽器
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


browser.get("https://shopee.tw/APPLE-iPhone-13-128G-%E7%8F%BE%E8%B2%A8-%E9%96%80%E5%B8%82%E7%8F%BE%E5%A0%B4%E4%BF%9D%E8%B2%BC%E6%9C%8D%E5%8B%99%E5%85%8C%E6%8F%9B%E5%88%B8-%E7%A5%9E%E8%85%A6%E7%94%9F%E6%B4%BB-i.54598032.13010000702?xptdk=daa1869a-72b8-45ca-81d3-0ffbebbf6932")

source = browser.page_source

## 發送請求 → 取得回應 → 網頁解析
soup = BeautifulSoup(source,"html.parser")


###商品名稱

# print(goodsName)
goodsName = soup.select_one("span[class=uYtT7n]").text
print(goodsName)

###商品價格
goodsPrice = soup.find('div', class_='pmmxKx')
print(goodsPrice.text)

###商品優惠
discount = soup.find('div', class_='lTuS3S')
print(discount.text)