from webcrolling import get_urls
from getdetaildata import get_detaildata
from getsummarydata import get_summarydata
import time
import csv

if __name__ == '__main__':
    start_time = time.time()

    #word = input()

    #category_urls = get_urls(word)e
    #get_summarydata(category_urls)

    urls = []
    urls.append("https://www.coupang.com/vp/products/7685497846?itemId=18559007860&vendorItemId=85588900949&pickType=COU_PICK&q=2023+%EC%82%BC%EC%84%B1%EB%85%B8%ED%8A%B8%EB%B6%81&itemsCount=36&searchId=6d6723c192af4c58861b0942e08394cf&rank=1&isAddedCart=")

    all_data = get_detaildata(urls)

    print(all_data)
    # for key, value in data.items():
    #     output_str = f'{key}: {value}'
    #     print(output_str)

    for data in all_data:
        with open('product.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data.values())



    print(f"--- data 추출 시간 : %s 초 ---" % (time.time() - start_time))