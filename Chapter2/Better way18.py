#
# 아이템 18
#

pictures = {}
path = 'profile_1234.png'

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'경로를 열 수 없습니다: {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()

try:
    handle = pictures.setdefault(path, open(path, 'a+b'))
except OSError:
    print(f'경로를 열 수 없습니다: {path}')
    raise
else:
    handle.seek(0)
    image_data = handle.read()

from collections import defaultdict

def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'경로를 열 수 없습니다: {profile_path}')
        raise

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#pictures = defaultdict(open_picture)
#handle = pictures[path]
#handle.seek(0)
#image_data = handle.read()

class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

