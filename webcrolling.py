import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def get_urls():
    big_urls = {}
    all_each_urls = {}
    word = input()

    options = uc.ChromeOptions()
    # 팝업 차단을 활성화합니다.
    options.add_argument('--disable-popup-blocking')

    #로그인 화면
    driver = uc.Chrome()
    driver.get("https://coupang.com/")

    # 검색
    search = driver.find_element(By.NAME, "q")
    search.send_keys(word)
    search.send_keys(Keys.RETURN)

    cupang_ranking = driver.current_url
    big_urls["쿠팡랭킹주소"] = cupang_ranking

    # 판매량 순
    salecount_ranking = cupang_ranking + "&sorter=saleCountDesc"
    big_urls["판매량주소"] = salecount_ranking

    # 낮은 가격 순
    salepriceasc_ranking = cupang_ranking + "&sorter=salePriceAsc"
    big_urls["낮은가격주소"] = salepriceasc_ranking

    #봇 인식 방지 BeautifulSoup
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    for each_category, each_url in big_urls.items():
        response = requests.get(each_url, headers=headers)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')
        # print(soup) #html 전체

        span_elements = soup.find_all('span', class_='number')

        geturls = []

        # 각 <span> 요소에서 부모인 <a> 요소의 내용 가져오기
        for span_element in span_elements:
            a_element = span_element.find_parent('a')
            if a_element:
                href_link = a_element['href']
                geturls.append('http://www.coupang.com' + href_link)

        all_each_urls[each_category+" top10 url"] = geturls

    print(big_urls)
    print(all_each_urls)

    return big_urls, all_each_urls
