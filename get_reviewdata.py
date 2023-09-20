from bs4 import BeautifulSoup as bs
from typing import Optional, Union, Dict, List
import time
import os
import re
import requests as rq
import json


def get_headers(
        key: str,
        default_value: Optional[str] = None
) -> Dict[str, Dict[str, str]]:
    """ Get Headers """
    JSON_FILE: str = 'headers.json'

    with open(JSON_FILE, 'r', encoding='UTF-8') as file:
        headers: Dict[str, Dict[str, str]] = json.loads(file.read())

    try:
        return headers[key]
    except:
        if default_value:
            return default_value
        raise EnvironmentError(f'Set the {key}')


class Coupang:
    @staticmethod
    def get_product_code(url: str) -> str:
        """ 입력받은 URL 주소의 PRODUCT CODE 추출하는 메소드 """
        prod_code: str = url.split('products/')[-1].split('?')[0]
        return prod_code

    def __init__(self) -> None:
        self.__headers: Dict[str, str] = get_headers(key='headers')

    def main(self, product_code) -> List[Dict[str,str]]:

        # URL 주소 재가공
        review_url = f'https://www.coupang.com/vp/product/reviews?productId={product_code}&page=1&size=5&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=3&ratingSummary=true'

        # __headers에 referer 키 추가
        self.__headers['referer'] = review_url

        with rq.Session() as session:
            return self.fetch(url=review_url, session=session)


    def fetch(self, url: str, session) -> List[Dict[str,str]]:
        save_data = []

        with session.get(url=url, headers=self.__headers) as response:
            html = response.text
            soup = bs(html, 'html.parser')

            # Article Boxes
            article_lenth = len(soup.select('article.sdp-review__article__list'))

            for idx in range(article_lenth):
                dict_data = {}
                articles = soup.select('article.sdp-review__article__list')

                # 평점
                rating = articles[idx].select_one('div.sdp-review__article__list__info__product-info__star-orange')
                if rating == None:
                    rating = 0
                else:
                    rating = int(rating.attrs['data-rating'])

                # 구매자 상품명
                prod_name = articles[idx].select_one('div.sdp-review__article__list__info__product-info__name')
                if prod_name == None or prod_name.text == '':
                    prod_name = '-'
                else:
                    prod_name = prod_name.text.strip()

                # 헤드라인(타이틀)
                headline = articles[idx].select_one('div.sdp-review__article__list__headline')
                if headline == None or headline.text == '':
                    headline = '등록된 헤드라인이 없습니다'
                else:
                    headline = headline.text.strip()

                # 리뷰 내용
                review_content = articles[idx].select_one('div.sdp-review__article__list__review > div')
                if review_content == None:
                    review_content = '등록된 리뷰내용이 없습니다'
                else:
                    review_content = re.sub('[\n\t]', '', review_content.text.strip())

                # 맛 만족도
                answer = articles[idx].select_one('span.sdp-review__article__list__survey__row__answer')
                if answer == None or answer.text == '':
                    answer = '맛 평가 없음'
                else:
                    answer = answer.text.strip()

                dict_data['prod_name'] = prod_name
                dict_data['rating'] = rating
                dict_data['headline'] = headline
                dict_data['review_content'] = review_content
                dict_data['answer'] = answer

                save_data.append(dict_data)

            time.sleep(1)

            return save_data



