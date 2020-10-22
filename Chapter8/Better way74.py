#
# 아이템 74
#

def timecode_to_index(video_id, timecode):
    return 1243
    # 비디오 데이터의 바이트 오프셋을 반환한다


def request_chunk(video_id, byte_offset, size):
    pass
    # video_id에 대한 비디오 데이터 중에 바이트 오프셋부터 size만큼을 반환한다


video_id = ...
timecode = '01:09:14:28'
byte_offset = timecode_to_index(video_id, timecode)
size = 20 * 1024 * 1024
video_data = request_chunk(video_id, byte_offset, size)

# 책에는 없지만 실행을 시키기 위해 추가한 코드
# 소켓을 에뮬레이션
import os

class NullSocket:
    def __init__(self):
        self.handle = open(os.devnull, 'wb')

    def send(self, data):
        self.handle.write(data)
# 책에는 없지만 실행을 시키기 위해 추가한 코드 끝

socket = ...            # 클라이언트가 연결한 소켓
video_data = ...        # video_id에 해당하는 데이터가 들어 있는 bytes
byte_offset = ...       # 요청받은 시작 위치
size = 20 * 1024 * 1024 # 요정받은 데이터 크기

# 책에는 없지만 실행을 시키기 위해 추가한 코드
socket = NullSocket()
video_data = 100 * os.urandom(1024 * 1024)
byte_offset = 1234
# 책에는 없지만 실행을 시키기 위해 추가한 코드 끝

chunk = video_data[byte_offset:byte_offset + size]
socket.send(chunk)

#
import timeit

video_data = 100 * os.urandom(1024 * 1024)
byte_offset = 1234

def run_test():
    chunk = video_data[byte_offset:byte_offset + size]
    # socket.send(chunk)를 호출해야 하지만 벤치마크를 위해 무시한다

result = timeit.timeit(
    stmt='run_test()',
    globals=globals(),
    number=100) / 100

print(f'{result:0.9f} 초')

#
data = '동해물과 abc 백두산이 마르고 닳도록'.encode("utf8")
view = memoryview(data)
chunk = view[12:19]
print(chunk)
print('크기      :', chunk.nbytes)
print('뷰의 데이터:', chunk.tobytes())
print('내부 데이터:', chunk.obj)

#
video_view = memoryview(video_data)

def run_test():
    chunk = video_view[byte_offset:byte_offset + size]
    # socket.send(chunk)를 호출해야 하지만 벤치마크를 위해 무시한다

result = timeit.timeit(
    stmt='run_test()',
    globals=globals(),
    number=100) / 100

print(f'{result:0.9f} 초')

#
socket = ...       # 클라이언트가 연결한 소켓
video_cache = ...  # 서버로 들어오는 비디오 스트림의 캐시
byte_offset = ...  # 데이터 버퍼 위치
size = 1024 * 1024 # 데이터 덩어리 크기

# 책에는 없지만 실행을 시키기 위해 추가한 코드
# 소켓을 에뮬레이션
class FakeSocket:

    def recv(self, size):
        return video_view[byte_offset:byte_offset+size]

    def recv_into(self, buffer):
        source_data = video_view[byte_offset:byte_offset+size]
        buffer[:] = source_data

socket = FakeSocket()
video_cache = video_data[:]
byte_offset = 1234
# 책에는 없지만 실행을 시키기 위해 추가한 코드 끝

chunk = socket.recv(size)
video_view = memoryview(video_cache)
before = video_view[:byte_offset]
after = video_view[byte_offset + size:]
new_cache = b''.join([before, chunk, after])

#
class FakeSocket:

    def recv(self, size):
        return video_view[byte_offset:byte_offset+size]

    def recv_into(self, buffer):
        source_data = video_view[byte_offset:byte_offset+size]
        buffer[:] = source_data

size = 1024 * 1024
socket = FakeSocket()
video_cache = video_data[:]
byte_offset = 1234

chunk = socket.recv(size)
video_view = memoryview(video_cache)
before = video_view[:byte_offset]
after = video_view[byte_offset + size:]
new_cache = b''.join([before, chunk, after])

def run_test():
    chunk = socket.recv(size)
    before = video_view[:byte_offset]
    after = video_view[byte_offset + size:]
    new_cache = b''.join([before, chunk, after])

result = timeit.timeit(
    stmt='run_test()',
    globals=globals(),
    number=100) / 100

print(f'{result:0.9f} 초')

#
my_bytes = b'hello'
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#my_bytes[0] = b'\x79'

#
my_array = bytearray('hello 안녕'.encode("utf8"))
my_array[0] = 0x79
print(my_array)

#
my_array = bytearray('row, row, row your 보트'.encode("utf8"))
my_view = memoryview(my_array)
write_view = my_view[3:13]
write_view[:] = b'-10 bytes-'
print(my_array)

#

video_array = bytearray(video_cache)
write_view = memoryview(video_array)
chunk = write_view[byte_offset:byte_offset + size]
socket.recv_into(chunk)

def run_test():
    chunk = write_view[byte_offset:byte_offset + size]
    socket.recv_into(chunk)

result = timeit.timeit(
    stmt='run_test()',
    globals=globals(),
    number=100) / 100

print(f'{result:0.9f} seconds')

