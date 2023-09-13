from webcrolling import get_urls
from getdetaildata import get_detaildata
from getsummarydata import get_summarydata
import time

if __name__ == '__main__':
    start_time = time.time()

    word = input()

    #category_urls = get_urls(word)
    #get_summarydata(category_urls)
    print(get_detaildata("https://www.coupang.com/vp/products/5625704601?itemId=9133866800&vendorItemId=79544780507&q=.%EC%83%9D%EC%88%98&itemsCount=36&searchId=b7155afb588e43c08928a4f10c405034&rank=1&isAddedCart="))


    print(f"--- data 추출 시간 : %s 초 ---" % (time.time() - start_time))