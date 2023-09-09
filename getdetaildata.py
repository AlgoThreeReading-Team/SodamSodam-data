import requests
from bs4 import BeautifulSoup

def getdata():
    #봇 인식 방지 BeautifulSoup
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    response = requests.get("http://www.coupang.com/vp/products/6006314977?itemId=1036057927&vendorItemId=5489327048&pickType=COU_PICK", headers=headers)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all('h2', class_='prod-buy-header-title')
    original_price = soup.find_all('span', class_='origin-price')
    discount_price = soup.find_all('span', class_='total-price')
    discount_percent = soup.find_all('span', class_='discount-rate')

    print(str(title) + "\n" + str(original_price) + "\n" + str(discount_price) + "\n" + str(discount_percent))