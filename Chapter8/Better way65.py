#
# 아이템 65
#

def try_finally_example(filename):
    print('* 파일 열기')
    handle = open(filename, encoding='utf-8') # OSError 발생할 수 있음
    try:
        print('* 데이터 읽기')
        return handle.read()      # UnicodeDecodeError 발생할 수 있음
    finally:
        print('* close() 호출')
        handle.close()            # try 블록이 실행된 다음에는 항상 이 블록이 실행됨


filename = 'random_data.txt'

with open(filename, 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')  # 잘못된 utf-8 이진 문자열

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#data = try_finally_example(filename)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#try_finally_example('does_not_exist.txt')

#
import json

def load_json_key(data, key):
    try:
        print('* JSON 데이터 읽기')
        result_dict = json.loads(data)     # ValueError가 발생할 수 있음
    except ValueError as e:
        print('* ValueError 처리')
        raise KeyError(key) from e
    else:
        print('* 키 검색')
        return result_dict[key]            # KeyError가 발생할 수 있음

assert load_json_key('{"foo": "bar"}', 'foo') == 'bar'

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#load_json_key('{"foo": bad payload', 'foo')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#load_json_key('{"foo": "bar"}', '존재하지 않음')

#
UNDEFINED = object()

def divide_json(path):
    print('* 파일 열기')
    handle = open(path, 'r+')             # OSError가 발생할 수 있음
    try:
        print('* 데이터 읽기')
        data = handle.read()              # UnicodeDecodeError가 발생할 수 있음
        print('* JSON 데이터 읽기')
        op = json.loads(data)             # ValueError가 발생할 수 있음
        print('* 계산 수행')
        value = (
            op['numerator'] /
            op['denominator'])            # ZeroDivisionError가 발생할 수 있음
    except ZeroDivisionError as e:
        print('* ZeroDivisionError 처리')
        return UNDEFINED
    else:
        print('* 계산 결과 쓰기')
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)                    # OSError가 발생할 수 있음
        handle.write(result)              # OSError가 발생할 수 있음
        return value
    finally:
        print('* close() 호출')
        handle.close()                    # 어떤 경우든 실행됨

temp_path = 'random_data.json'

with open(temp_path, 'w') as f:
    f.write('{"numerator": 1, "denominator": 10}')

assert divide_json(temp_path) == 0.1

#
with open(temp_path, 'w') as f:
    f.write('{"numerator": 1, "denominator": 0}')

assert divide_json(temp_path) is UNDEFINED

#
with open(temp_path, 'w') as f:
    f.write('{"numerator": 1 bad data')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#divide_json(temp_path)

