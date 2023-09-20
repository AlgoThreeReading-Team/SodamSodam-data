import requests
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from imagetotext import image_text
from get_reviewdata import Coupang
def get_detaildata(product_url):
    driver = uc.Chrome()

    #봇 인식 방지 BeautifulSoup
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}


    response = requests.get(product_url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h2', class_='prod-buy-header__title').text
    image_url = "https:" + soup.find('img', class_='prod-image__detail')['src']
    total_price = soup.find('span', class_='total-price').text.split()[0]
    shipping_fee = soup.find('div', class_='prod-shipping-fee-message').text.split()
    shipping_fee_detail = " ".join(shipping_fee[1:]).strip()

    if soup.find('div', class_='prod-shipping-fee-message'):
        shipping_fee = soup.find('div', class_='prod-shipping-fee-message').text.split()
        shipping_fee_detail = " ".join(shipping_fee[1:]).strip()
    else:
        shipping_fee = "shipping_fee null"


    if shipping_fee_detail == "":
       shipping_fee_detail = "shipping_fee_detail null"
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

    # 자바 스크립트
    driver.get(product_url)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #필수 표기 정보
    essential_info = {}

    rows = soup.find('table', 'prod-delivery-return-policy-table')
    for row in rows.find_all('tr'):
        th = row.find('th').text
        td = row.find('td').text
        essential_info[th] = td


    #상품 상세 내용
    big_content = soup.find('div', class_='vendor-item')

    # 이미지 URL 추출
    image_urls = []
    img_tags = big_content.find_all('img')
    for img_tag in img_tags:
        src = img_tag['src']
        if src:
            if not src.startswith('http'):
                src = 'https:' + src
            image_urls.append(src)

    image_convert = image_text(image_urls) #이미지 text화

    # 텍스트 추출
    text_list = []
    text_divs = big_content.find_all('div', class_='subType-TEXT')
    for text_div in text_divs:
        text = text_div.text
        text_list.append(text)

    # 리뷰 추출
    product_code = product_url.split('products/')[-1].split('?')[0]
    review_datas = Coupang().main(product_code)


    each_data = {
        "title" : title,
        "product_url" : product_url,
        "image_url" : image_url,
        "total_price" : total_price,
        "shipping_fee" : shipping_fee,
        "shipping_fee_detail" : shipping_fee_detail,
        "original_price" : original_price,
        "discount_percent" : discount_percent,
        "delivery_day" : delivery_day,
        "essential_info" : essential_info,
        "image_text" : image_convert,
        "text" : text_list,
        "review" : review_datas
    }

    driver.quit()
    return each_data