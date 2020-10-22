###
### 아이템 5
###

from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=',
                     keep_blank_values=True)
print(repr(my_values))

print('빨강: ', my_values.get('빨강'))
print('초록: ', my_values.get('초록'))
print('투명도: ', my_values.get('투명도'))


# 질의 문자열이 `빨강=5&파랑=0&초록='인 경우
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('파랑', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0
print(f'빨강: {red!r}')
print(f'초록: {green!r}')
print(f'투명도: {opacity!r}')

red = int(my_values.get('빨강', [''])[0] or 0)

red_str = my_values.get('빨강', [''])
red = int(red_str[0]) if red_str[0] else 0

green_str = my_values.get('초록', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
    
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, '초록')

