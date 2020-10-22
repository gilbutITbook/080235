#
# 아이템 12
#
x = ['빨강', '주황', '노랑', '녹색', '파랑', '자주']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = b'mongoose'
y = x[::-1]
print(y)

x = '寿司'
y = x[::-1]
print(y)

w = '寿司'
x = w.encode('utf-8')
y = x[::-1]
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#z = y.decode('utf-8')

w = 'abcZYX123'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
print(z)

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x[::2] # ['a', 'c', 'e', 'g']
x[::-2] # ['h', 'f', 'd', 'b']

x[2::2]    # ['c', 'e', 'g']
x[-2::-2]  # ['g', 'e', 'c', 'a']
x[-2:2:-2] # ['g', 'e']
x[2:2:-2]  # []

y = x[::2] # ['a', 'c', 'e', 'g']
z = y[1:-1] # ['c', 'e']
