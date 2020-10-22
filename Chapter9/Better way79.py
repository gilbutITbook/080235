#
# 아이템 79
#
class ZooDatabase:
    ...

    def get_animals(self, species):
        ...

    def get_food_period(self, species):
        ...

    def feed_animal(self, name, when):
        ...

from datetime import datetime

def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = database.get_food_period(species)
    animals = database.get_animals(species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) >= feeding_timedelta:
            database.feed_animal(name, now)
            fed += 1
    return fed

from unittest.mock import Mock

database = Mock(spec=ZooDatabase)
print(database.feed_animal)
database.feed_animal()
database.feed_animal.assert_any_call()

#
from datetime import timedelta
from unittest.mock import call

now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2019, 6, 5, 15, 45)

database = Mock(spec=ZooDatabase)
database.get_food_period.return_value = timedelta(hours=3)
database.get_animals.return_value = [
    ('점박이', datetime(2019, 6, 5, 11, 15)),
    ('털보', datetime(2019, 6, 5, 12, 30)),
    ('조조', datetime(2019, 6, 5, 12, 55))
]

result = do_rounds(database, '미어캣', utcnow=now_func)
assert result == 2

database.get_food_period.assert_called_once_with('미어캣')
database.get_animals.assert_called_once_with('미어캣')
database.feed_animal.assert_has_calls(
    [
        call('점박이', now_func.return_value),
        call('털보', now_func.return_value),
    ],
    any_order=True)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#database.bad_method_name()


DATABASE = None

def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase()
    return DATABASE

def main(argv):
    database = get_database()
    species = argv[1]
    count = do_rounds(database, species)
    print(f'급양: {count} {species}')
    return 0

#
import contextlib
import io
from unittest.mock import patch

with patch('__main__.DATABASE', spec=ZooDatabase):
    now = datetime.utcnow()

    DATABASE.get_food_period.return_value = timedelta(hours=3)
    DATABASE.get_animals.return_value = [
        ('점박이', now - timedelta(minutes=4.5)),
        ('털보', now - timedelta(hours=3.25)),
        ('조조', now - timedelta(hours=3)),
    ]

    fake_stdout = io.StringIO()
    with contextlib.redirect_stdout(fake_stdout):
        main(['프로그램 이름', '미어캣'])

    found = fake_stdout.getvalue()
    expected = '급양: 2 미어캣\n'

    assert found == expected

