###
### 아이템 3
###
a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c'))) # UTF-8에서 한글은 3바이트임

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))

print(b'one' + b'two')
print('one' + 'two')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# b'one' + 'two'   # TypeError

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# 'one' + b'two'   # TypeError


assert b'red' > b'blue'
assert 'red' > 'blue'

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# assert 'red' > b'blue'  # TypeError

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#assert b'blue' < 'red'  # TypeError

print(b'foo' == 'foo')  # 항상 false

print(b'red %s' % b'blue')  # 타입이 같은 형식화문자열 사용
print('red %s' % 'blue')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#print(b'red %s' % 'blue')   # TypeError

print('red %s' % b'blue')   # 생각과 다르게 작동

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#with open('data.bin', 'w') as f:  # TypeError
#    f.write(b'\xf1\xf2\xf3\xf4\xf5')

with open('data.bin', 'wb') as f:   
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#with open('data.bin', 'r') as f:   # UnicodeDecodeError
#    data = f.read()

with open('data.bin', 'rb') as f:
    data = f.read()

with open('data.bin', 'r', encoding='cp1252') as f:
    data = f.read()
    
assert data == 'ñòóôõ'

# 시스템 인코딩 검사: python3 -c 'import locale; print(locale.getpreferredencoding())'
