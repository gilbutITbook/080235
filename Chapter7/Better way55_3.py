from queue import Queue
from threading import Thread
import time

my_queue = Queue(1)  # 버퍼 크기 1

def consumer():
    time.sleep(0.1)  # 대기
    my_queue.get()  # 두 번째로 실행됨
    print('소비자 1')
    my_queue.get()  # 네 번째로 실행됨
    print('소비자 2')
    print('소비자 완료')

thread = Thread(target=consumer)
thread.start()

my_queue.put(object()) # 첫 번째로 실행됨
print('생산자 1')
my_queue.put(object()) # 세 번째로 실행됨
print('생산자 2')
print('생산자 완료')
thread.join()
