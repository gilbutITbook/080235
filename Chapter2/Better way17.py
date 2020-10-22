#
# 아이템 17
#
visits = {
    '미국': {'뉴욕', '로스엔젤레스'},
    '일본': {'하코네'},
}

visits.setdefault('프랑스', set()).add('칸') # 짧다

if (japan := visits.get('일본')) is None:      # 길다
    visits['일본'] = japan = set()

japan.add('교토')

print(visits)


class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)

visits = Visits()
visits.add('러시아', '예카테린부르크')
visits.add('탄자니아', '잔지바르')
print(visits.data)

from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('영국', '바스')
visits.add('영국', '런던')
print(visits.data)
