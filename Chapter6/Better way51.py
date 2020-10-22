#
# 아이템 51
#
from functools import wraps

def trace_func(func):
    if hasattr(func, 'tracing'):  # 단 한번만 데코레이터를 적용한다
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f'{func.__name__}({args!r}, {kwargs!r}) -> '
                  f'{result!r}')

    wrapper.tracing = True
    return wrapper

class TraceDict(dict):
    @trace_func
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @trace_func
    def __setitem__(self, *args, **kwargs):
        return super().__setitem__(*args, **kwargs)

    @trace_func
    def __getitem__(self, *args, **kwargs):
        return super().__getitem__(*args, **kwargs)


trace_dict = TraceDict([('안녕', 1)])
trace_dict['거기'] = 2
trace_dict['안녕']
try:
    trace_dict['존재하지 않음']
except KeyError:
    pass # 키 오류가 발생할 것으로 예상함

#
import types

trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType)


class TraceMeta(type):
    def __new__(meta, name, bases, class_dict):
        klass = super().__new__(meta, name, bases, class_dict)

        for key in dir(klass):
            value = getattr(klass, key)
            if isinstance(value, trace_types):
                wrapped = trace_func(value)
                setattr(klass, key, wrapped)

        return klass


class TraceDict(dict, metaclass=TraceMeta):
    pass

trace_dict = TraceDict([('안녕', 1)])
trace_dict['거기'] = 2
trace_dict['안녕']
try:
    trace_dict['존재하지 않음']
except KeyError:
    pass # 키 오류가 발생할 것으로 예상함

#
def my_class_decorator(klass):
    klass.extra_param = '안녕'
    return klass

@my_class_decorator
class MyClass:
    pass

print(MyClass)
print(MyClass.extra_param)

#
def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass


@trace
class TraceDict(dict):
    pass

trace_dict = TraceDict([('안녕', 1)])
trace_dict['거기'] = 2
trace_dict['안녕']
try:
    trace_dict['존재하지 않음']
except KeyError:
    pass # 키 오류가 발생할 것으로 예상함
