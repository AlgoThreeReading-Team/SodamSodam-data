from webcrolling import get_urls
from getdetaildata import get_detaildata
from getsummarydata import get_summarydata
import time

if __name__ == '__main__':
    start_time = time.time()

    word = input()

    #category_urls = get_urls(word)
    #get_summarydata(category_urls)
    data = get_detaildata("https://www.coupang.com/vp/products/6006314977?itemId=1036057927&vendorItemId=5489327048&pickType=COU_PICK&q=%EA%B3%A0%EA%B5%AC%EB%A7%88&itemsCount=35&searchId=ad0db04a78e54e838a709712b89014b0&rank=1&isAddedCart=")

    for key, value in data.items():
        output_str = f'{key}: {value}'
        print(output_str)



    print(f"--- data 추출 시간 : %s 초 ---" % (time.time() - start_time))