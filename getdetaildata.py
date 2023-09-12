import requests
from bs4 import BeautifulSoup

def getdata(all_each_urls):
    all_data = []
    #봇 인식 방지 BeautifulSoup
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    for each_category, each_urls in all_each_urls.items():
        for each_url in each_urls:
            response = requests.get(each_url, headers=headers)
            html = response.content

            soup = BeautifulSoup(html, 'html.parser')

            title = soup.find('h2', class_='prod-buy-header__title').text
            image_url = "https:" + soup.find('img', class_='prod-image__detail')['src']
            total_price = soup.find('span', class_='total-price').text.split()[0]
            shipping_fee = soup.find('div', class_='prod-shipping-fee-message').text.split()
            shipping_fee_detail = " ".join(shipping_fee[1:]).strip()

            if shipping_fee_detail == "":
                shipping_fee_detail = "shipping_fee_detail_null"
            shipping_fee = shipping_fee[0].strip()

            if soup.find('span', class_='origin-price'):
                original_price = soup.find('span', class_='origin-price').text.strip()
            else:
                original_price = "original_price null"

            if soup.find('span', class_='discount-rate'):
                discount_percent = soup.find('span', class_='discount-rate').text.strip()
            else:
                discount_percent = "discount_percent null"

            if soup.find('div', class_='prod-pdd-display-area PDD_DISPLAY_0'):
                delivery_day = soup.find('div', class_='prod-pdd-display-area').text.strip()
            else:
                delivery_day = "deliver_day null"

            each_data = {
                "category" : each_category,
                "title" : title,
                "product_url" : each_url,
                "image_url" : image_url,
                "total_price" : total_price,
                "shipping_fee" : shipping_fee,
                "shipping_fee_detail" : shipping_fee_detail,
                "original_price" : original_price,
                "discount_percent" : discount_percent,
                "delivery_day" : delivery_day
            }

            all_data.append(each_data)

    return all_data