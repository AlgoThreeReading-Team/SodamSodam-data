import requests
from bs4 import BeautifulSoup

def get_summarydata(category_urls):
    # 봇 인식 방지 BeautifulSoup
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    for category_url in category_urls:
        response = requests.get(category_url, headers=headers)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')
        span_elements = soup.find_all('span', class_='number')

        get_datalist = []
        # 각 <span> 요소에서 부모인 <a> 요소의 내용 가져오기
        for span_element in span_elements:
            summarydata = {}
            a_element = span_element.find_parent('a')
            if a_element:
                summarydata["product_url"] = 'http://www.coupang.com' + a_element['href']
                summarydata["image_url"] = 'http://www.coupang.com' + a_element.find('img', class_='search-product-wrap-img')['src']
                summarydata["title"] = a_element.find('div', class_='name').text.strip()

                if a_element.find('span', class_='price-info'):
                    summarydata["discount_rate"] = a_element.find('span', class_='instant-discount-rate').text.strip()
                    summarydata["origin-price"] = a_element.find('del', class_='base-price').text.strip()
                else:
                    summarydata["discount_rate"] = "discount_rate null"
                    summarydata["origin_price"] = "origin_price null"

                summarydata["price_value"] = a_element.find('em', class_='sale').text.strip()
                summarydata["delivery"] = a_element.find('div', class_='delivery').text.strip()
                summarydata["avg-star"] = a_element.find('span', class_='star').text.strip()
                summarydata['count-star'] = a_element.find('span',class_='rating-total-count').text.strip()

                get_datalist.append(summarydata)

        print(get_datalist)
