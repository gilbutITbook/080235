import select
import socket
import time

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()

for _ in range(5):
    slow_systemcall()

end = time.time()
delta = end - start
print(f'총 {delta:.3f} 초 걸림')
