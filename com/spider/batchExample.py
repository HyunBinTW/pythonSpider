from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://hiskio.com/fundraising/527/about")
print(browser.page_source)
browser.quit()
# url = 'https://hiskio.com/fundraising/527/about'
# r = requests.get(url)
# response = r.text
# soup = BeautifulSoup(r.text,"html.parser")
#
# print(soup)



