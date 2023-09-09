import requests
from bs4 import BeautifulSoup

def getdata(all_each_urls):
    #봇 인식 방지 BeautifulSoup
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    for each_category, each_urls in all_each_urls.items():
        print(each_category)
        count = 0
        for each_url in each_urls:
            response = requests.get(each_url, headers=headers)
            html = response.content

            soup = BeautifulSoup(html, 'html.parser')


            title = soup.find_all('h2', class_='prod-buy-header__title')[0].text
            image_url = "https:" + soup.find_all('img', class_='prod-image__detail')[0]['src']
            total_price = soup.find_all('span', class_='total-price')[0].text.split()[0]
            shipping_fee = soup.find_all('div', class_='prod-shipping-fee-message')[0].text.split()

            if soup.find_all('span', class_='origin-price'):
                original_price = soup.find_all('span', class_='origin-price')[0].text.split()[0]
            if soup.find_all('span', class_='discount-rate'):
                discount_percent = soup.find_all('span', class_='discount-rate')[0].text.split()[0]
            if soup.find_all('div', class_='prod-pdd-display-area'):
                delivery_day = soup.find_all('div', class_='prod-pdd-display-area')[0].text.split()

            count = count + 1
            print(count)
            print(title + "\n" + image_url + "\n" +original_price + "\n" + total_price + "\n" + discount_percent + "\n" + str(shipping_fee) + "\n" + str(delivery_day))

