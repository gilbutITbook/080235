#
# 아이템 78
#
class DatabaseConnection:
    def __init__(self, host, port):
        pass


def get_animals(database, species):
    # 데이터베이스에 질의한다
    ...
    # (이름, 급양시간) 튜플 리스트를 반환한다

database = DatabaseConnection('localhost', '4444')

get_animals(database, '미어캣')

#
from datetime import datetime
from unittest.mock import Mock

def get_animals(database, species):
    # 데이터베이스에 질의한다
    ...
    # (이름, 급양시간) 튜플 리스트를 반환한다
    return [("", datetime(2020,1,1,1,1,1))]


mock = Mock(spec=get_animals)
expected = [
    ('점박이', datetime(2020, 6, 5, 11, 15)),
    ('털보', datetime(2020, 6, 5, 12, 30)),
    ('조조', datetime(2020, 6, 5, 12, 45)),
]
mock.return_value = expected

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#mock.does_not_exist

database = object()
result = mock(database, '미어캣')
assert result == expected

#
mock.assert_called_once_with(database, '미어캣')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#mock.assert_called_once_with(database, '기린')

#
from unittest.mock import ANY

mock = Mock(spec=get_animals)
mock('database 1', '토끼')
mock('database 2', '들소')
mock('database 3', '미어캣')

mock.assert_called_with(ANY, '미어캣')

#
class MyError(Exception):
    pass

mock = Mock(spec=get_animals)
mock.side_effect = MyError('애그머니나! 큰 문제 발생')
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#result = mock(database, '미어캣')

#
def get_food_period(database, species):
    # 데이터베이스에 질의한다
    ...
    # 주기를 반환한다
    return 3


def feed_animal(database, name, when):
    # 데이터베이스에 기록한다
    ...


def do_rounds(database, species):
    now = datetime.datetime.utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1
    return fed

def do_rounds(database, species, *,
              now_func=datetime.utcnow,
              food_func=get_food_period,
              animals_func=get_animals,
              feed_func=feed_animal):
    now = now_func()
    feeding_timedelta = food_func(database, species)
    animals = animals_func(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_func(database, name, now)
            fed += 1
    return fed

from datetime import datetime
from datetime import timedelta

now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2020, 6, 5, 15, 45)

food_func = Mock(spec=get_food_period)
food_func.return_value = timedelta(hours=3)

animals_func = Mock(spec=get_animals)
animals_func.return_value = [
    ('점박이', datetime(2020, 6, 5, 11, 15)),
    ('털보', datetime(2020, 6, 5, 12, 30)),
    ('조조', datetime(2020, 6, 5, 12, 45)),
]

feed_func = Mock(spec=feed_animal)

result = do_rounds(
    database,
    '미어캣',
    now_func=now_func,
    food_func=food_func,
    animals_func=animals_func,
    feed_func=feed_func)

assert result == 2

from unittest.mock import call

food_func.assert_called_once_with(database, '미어캣')

animals_func.assert_called_once_with(database, '미어캣')

feed_func.assert_has_calls(
    [
        call(database, '점박이', now_func.return_value),
        call(database, '털보', now_func.return_value),
    ],
    any_order=True)

#
from unittest.mock import patch

print('패치 외부:', get_animals)

with patch('__main__.get_animals'):
    print('패치 내부: ', get_animals)

print('다시 외부:', get_animals)

#
fake_now = datetime(2020, 6, 5, 15, 45)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#with patch('datetime.datetime.utcnow'):
#    datetime.utcnow.return_value = fake_now

#
def get_do_rounds_time():
    return datetime.datetime.utcnow()


def do_rounds(database, species):
    now = get_do_rounds_time()
    ...


with patch('__main__.get_do_rounds_time'):
    ...

#
def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_func(database, name, now)
            fed += 1

    return fed

#
from unittest.mock import DEFAULT

with patch.multiple('__main__',
                    autospec=True,
                    get_food_period=DEFAULT,
                    get_animals=DEFAULT,
                    feed_animal=DEFAULT):
    now_func = Mock(spec=datetime.utcnow)
    now_func.return_value = datetime(2020, 6, 5, 15, 45)
    get_food_period.return_value = timedelta(hours=3)
    get_animals.return_value = [
        ('점박이', datetime(2020, 6, 5, 11, 15)),
        ('털보', datetime(2020, 6, 5, 12, 30)),
        ('조조', datetime(2020, 6, 5, 12, 45))
    ]

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#result = do_rounds(database, '미어캣', utcnow=now_func)
#assert result == 2

food_func.assert_called_once_with(database, '미어캣')
animals_func.assert_called_once_with(database, '미어캣')
feed_func.assert_has_calls(
    [
        call(database, '점박이', now_func.return_value),
        call(database, '털보', now_func.return_value),
    ],
    any_order=True)

