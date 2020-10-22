from queue import Queue
from threading import Thread

my_queue = Queue()

def consumer():
    print('소비자 대기')
    my_queue.get()  # 다음에 보여줄 put()이 실행된 다음에 시행된다
    print('소비자 완료')

thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
my_queue.put(object())     # 앞에서 본 get()이 실행되기 전에 실행된다.
print('생산자 완료')
thread.join()

