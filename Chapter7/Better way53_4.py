import select
import socket
import time
from threading import Thread

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()

threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'총 {delta:.3f} 초 걸림')
