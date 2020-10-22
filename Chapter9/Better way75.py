#
# 아이템 75
#
print('foo 뭐시기')

my_value = 'foo 뭐시기'
print(str(my_value))
print('%s' % my_value)
print(f'{my_value}')
print(format(my_value))
print(my_value.__format__('s'))
print(my_value.__str__())

print(5)
print('5')

int_value = 5
str_value = '5'
print(f'{int_value} == {str_value} ?')

a = '\x07'
print(repr(a))

b = eval(repr(a))
assert a == b

print(repr(5))
print(repr('5'))

print('%r' % 5)
print('%r' % '5')

int_value = 5
str_value = '5'
print(f'{int_value!r} != {str_value!r}')

class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 'foo')
print(obj)


class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'BetterClass({self.x!r}, {self.y!r})'

obj = BetterClass(2, '뭐시기')
print(obj)

obj = OpaqueClass(4, 'baz')
print(obj.__dict__)

