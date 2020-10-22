#
# 아이템 42
#
class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

foo = MyObject()
assert foo.public_field == 5

assert foo.get_private_field() == 10

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#foo.__private_field

#
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


class MyParentObject:
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#baz.get_private_field()

# 문제없음
assert baz._MyParentObject__private_field == 71

print(baz.__dict__)

#
class MyStringClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

foo = MyStringClass(5)
assert foo.get_value() == '5'

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass('5')
assert foo.get_value() == 5

class MyBaseClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())  # 변경됨

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)  # 변경되지 않음

foo = MyIntegerSubclass(5)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#foo.get_value()

#
class ApiClass:
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # 충돌

a = Child()
print(f'{a.get()} 와 {a._value} 는 달라야 합니다.')

#
class ApiClass:
    def __init__(self):
        self.__value = 5    # 밑줄 2개!

    def get(self):
        return self.__value # 밑줄 2개!

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' # OK!

a = Child()
print(f'{a.get()} 와 {a._value} 는 다릅니다.')

