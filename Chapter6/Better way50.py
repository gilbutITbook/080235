#
# 아이템 50
#
class Field:
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

class Customer:
    # 클래스 애트리뷰트
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

cust = Customer()
print(f'이전: {cust.first_name!r} {cust.__dict__}')
cust.first_name = '유클리드'
print(f'이후: {cust.first_name!r} {cust.__dict__}')


#
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls

class DatabaseRow(metaclass=Meta):
    pass


class Field:
    def __init__(self):
        # 이 두 정보를 메타클래스가 채워 준다
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

cust = BetterCustomer()
print(f'이전: {cust.first_name!r} {cust.__dict__}')
cust.first_name = '오일러'
print(f'이후: {cust.first_name!r} {cust.__dict__}')

#
class BrokenCustomer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

cust = BrokenCustomer()
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#cust.first_name = '메르센'

#
class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        # 클래스가 생성될 때 모든 스크립터에 대해 이 메서드가 호출된다
        self.name = name
        self.internal_name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class FixedCustomer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

cust = FixedCustomer()
print(f'이전: {cust.first_name!r} {cust.__dict__}')
cust.first_name = '메르센'
print(f'이후: {cust.first_name!r} {cust.__dict__}')

