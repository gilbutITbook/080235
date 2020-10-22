from queue import Queue
from threading import Thread
import time

in_queue = Queue()

def consumer():
    print('소비자 대기')
    work = in_queue.get()  # 두 번째로 실행됨
    print('소비자 작업중')
    # Doing work
    print('소비자 완료')
    in_queue.task_done()  # 세 번째로 실행됨

thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
in_queue.put(object())    # 첫 번째로 실행됨
print('생산자 대기')
in_queue.join()           # 네 번째로 실행됨
print('생산자 완료')
thread.join()
