import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def get_urls(word):
    category_urls = []

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
    driver.quit()
    category_urls.append(cupang_ranking)

    # 판매량 순
    salecount_ranking = cupang_ranking + "&sorter=saleCountDesc"
    category_urls.append(salecount_ranking)

    # 낮은 가격 순
    salepriceasc_ranking = cupang_ranking + "&sorter=salePriceAsc"
    category_urls.append(salepriceasc_ranking)


    return category_urls
