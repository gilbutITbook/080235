#
# 아이템 47
#
class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'{name}의 값'
        setattr(self, name, value)
        return value

data = LazyRecord()
print('이전:', data.__dict__)
print('foo:', data.foo)
print('이후:', data.__dict__)

#
class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* 호출: __getattr__({name!r}), '
              f'인스턴스 딕셔너리 채워 넣음')
        result = super().__getattr__(name)
        print(f'* 반환: {result!r}')
        return result

data = LoggingLazyRecord()
print('exists: ', data.exists)
print('첫 번째 foo: ', data.foo)
print('두 번째 foo: ', data.foo)

#
class ValidatingRecord:
    def __init__(self):
        self.exists = 5
    def __getattribute__(self, name):
        print(f'* 호출: __getattr__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* {name!r} 찾음, {value!r} 반환')
            return value
        except AttributeError:
            value = f'{name}을 위한 값'
            print(f'* {name!r}를 {value!r}로 설정')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
print('exists: ', data.exists)
print('첫 번째 foo: ', data.foo)
print('두 번째 foo: ', data.foo)

#
class MissingPropertyRecord:
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError(f'{name}을 찾을 수 없음')
        return 1 # 무조건 1 반환

data = MissingPropertyRecord()
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#data.bad_name


#
data = LoggingLazyRecord() # __getattr__을 구현
print('이전: ', data.__dict__)
print('최초에 foo가 있나: ', hasattr(data, 'foo'))
print('이후: ', data.__dict__)
print('다음에 foo가 있나: ', hasattr(data, 'foo'))

#
data = ValidatingRecord() # __getattribute__를 구현
print('최초에 foo가 있나: ', hasattr(data, 'foo'))
print('다음에 foo가 있나: ', hasattr(data, 'foo'))

#
class SavingRecord:
    def __setattr__(self, name, value):
        # 데이터를 데이터베이스 레코드에 저장한다
        super().__setattr__(name, value)

class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name, value):
        print(f'* 호출: __setattr__({name!r}, {value!r})')
        super().__setattr__(name, value)

data = LoggingSavingRecord()
print('이전: ', data.__dict__)
data.foo = 5
print('이후: ', data.__dict__)
data.foo = 7
print('최후:', data.__dict__)

#
class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}
    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        return self._data[name]

data = Brokedata = BrokenDictionaryRecord({'foo': 3})
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#data.foo

#
class DictionaryRecord:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

data = DictionaryRecord({'foo': 3})
print('foo: ', data.foo)

