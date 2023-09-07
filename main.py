from webcrolling import geturls
import time

if __name__ == '__main__':
    start_time = time.time()
    geturls()

    print(f"--- data 추출 시간 : %s 초 ---" % (time.time() - start_time))