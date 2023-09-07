import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def geturls():
    word = input()

    options = uc.ChromeOptions()
    # 팝업 차단을 활성화합니다.
    options.add_argument('--disable-popup-blocking')

    driver = uc.Chrome()
    driver.get("https://www.coupang.com/")
    time.sleep(1)

    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(word)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)

    current_url = driver.current_url
    driver.quit()
    print(current_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    response = requests.get(current_url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    #print(soup) #html 전체

    span_elements = soup.find_all('span', class_='number')

    geturls = []

    # 각 <span> 요소에서 부모인 <a> 요소의 내용 가져오기
    for span_element in span_elements:
        a_element = span_element.find_parent('a')
        if a_element:
            href_link = a_element['href']
            geturls.append('http://www.coupang.com' + href_link)
            print('http://www.coupang.com' + href_link)

    return geturls