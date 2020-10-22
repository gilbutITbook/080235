#
# 아이템 48
#
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* 실행: {name}의 메타 {meta}.__new__')
        print('기반클래스들:', bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)

class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass

#
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Polygon 클래스의 하위 클래스만 검증한다
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('다각형 변은 3개 이상이어야 함')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    sides = None # 하위 클래스는 이 애트리뷰트에 값을 지정해야 한다
    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3

class Rectangle(Polygon):
    sides = 4

class Nonagon(Polygon):
    sides = 9

assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260

#
print('class 이전')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class Line(Polygon):
#    print('sides 이전')
#    sides = 2
#    print('sides 이후')

print('class 이후')

#
class BetterPolygon:
    sides = None  # 하위클래스에서 이 애트리뷰트의 값을 지정해야 함

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('다각형 변은 3개 이상이어야 함')

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Hexagon(BetterPolygon):
    sides = 6

assert Hexagon.interior_angles() == 720

#
class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # Filled 클래스의 하위 클래스만 검증한다
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('Fill color must be supported')
        return type.__new__(meta, name, bases, class_dict)


class Filled(metaclass=ValidateFilled):
    color = None  # 모든 하위 클래스에서 이 애트리뷰트의 값을 지정해야 한다

print('class 이전')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class Point(BetterPolygon):
#    sides = 1

print('class 이후')

#
class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # Filled 클래스의 하위 클래스만 검증한다
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('지원하지 않는 color 값')
        return type.__new__(meta, name, bases, class_dict)

class Filled(metaclass=ValidateFilled):
    color = None  # 모든 하위 클래스에서 이 애트리뷰트의 값을 지정해야 한다

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class RedPentagon(Filled, Polygon):
#    color = 'red'
#    sides = 5

#
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # 루트 클래스가 아닌 경우만 검증한다
        if not class_dict.get('is_root'):
            if class_dict['sides'] < 3:
                raise ValueError('다각형 변은 3개 이상이어야 함')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    is_root = True
    sides = None  # 하위 클래스에서 이 애트리뷰트 값을 지정해야 한다

class ValidateFilledPolygon(ValidatePolygon):
    def __new__(meta, name, bases, class_dict):
        # 루트 클래스가 아닌 경우만 검증한다
        if not class_dict.get('is_root'):
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('지원하지 않는 color 값')
        return super().__new__(meta, name, bases, class_dict)

class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
    is_root = True
    color = None  # 하위 클래스에서 이 애트리뷰트 값을 지정해야 한다

class GreenPentagon(FilledPolygon):
    color = 'green'
    sides = 5

greenie = GreenPentagon()
assert isinstance(greenie, Polygon)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# 색 오류
#class OrangePentagon(FilledPolygon):
#    color = 'orange'
#    sides = 5

#
class Filled:
    color = None  # 하위 클래스에서 이 애트리뷰트 값을 지정해야 한다

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ('red', 'green', 'blue'):
            raise ValueError('지원하지 않는 color 값')

class RedTriangle(Filled, Polygon):
    color = 'red'
    sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)

#
print('class 이전')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class BlueLine(Filled, Polygon):
#    color = 'blue'
#    sides = 2

print('class 이후')

#
print('class 이전')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class BeigeSquare(Filled, Polygon):
#    color = 'beige'
#    sides = 4

print('class 이후')

#

class Top:
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'{cls}의 Top')

class Left(Top):
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'{cls}의 Left')


class Right(Top):
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'{cls}의 Right')


class Bottom(Left, Right):
    def __init_subclass__(cls):
        super().__init_subclass__()
        print(f'{cls}의 Bottom')

