def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item

from collections import deque
from threading import Lock

class MyQueue:
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()

from threading import Thread
import time

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01) # 할 일이 없음
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()

done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())

while len(done_queue.items) < 1000:
    # 기다리는 동안 유용한 작업을 수행한다
    pass

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print(f'{processed} 개의 아이템을 처리했습니다, '
      f'이때 폴링을 {polled} 번 했습니다.')

# 작업이 끝나도 무한대기함. 프로그램을 강제종료시킬것