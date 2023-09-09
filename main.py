from webcrolling import get_urls
from getdetaildata import getdata
import time

if __name__ == '__main__':
    start_time = time.time()
    get_urls()
    #getdata()

    print(f"--- data 추출 시간 : %s 초 ---" % (time.time() - start_time))