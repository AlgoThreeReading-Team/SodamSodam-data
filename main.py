from webcrolling import get_urls
from getdetaildata import get_detaildata
from getsummarydata import get_summarydata
import time
import csv

if __name__ == '__main__':
    start_time = time.time()

    #word = input()

    #category_urls = get_urls(word)
    #get_summarydata(category_urls)
    data = get_detaildata("https://www.coupang.com/vp/products/6372535763?itemId=13504507360&vendorItemId=86407673438&q=%EB%A1%9C%EC%85%98&itemsCount=36&searchId=fd45a1f9213247df9011f1adb0dd4843&rank=2&isAddedCart=")

    print(data)
    for key, value in data.items():
        output_str = f'{key}: {value}'
        print(output_str)

    with open('product.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())



    print(f"--- data 추출 시간 : %s 초 ---" % (time.time() - start_time))