#
# 아이템 14
#
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', 0.5),
    Tool('끌', 0.25),
]

print('미정렬:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\n정렬: ', tools)

tools.sort(key=lambda x: x.weight)
print('무게순 정렬:', tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('대소문자 구분:', places)
places.sort(key=lambda x: x.lower())
print('대소문자 무시:', places)

power_tools = [
    Tool('드릴', 4),
    Tool('원형 톱', 5),
    Tool('착암기', 40),
    Tool('연마기', 4),
]

saw = (5, '원형 톱')
jackhammer = (40, '착암기')
assert not (jackhammer < saw) # 예상한 대로 결과가 나온다

drill = (4, '드릴')
sander = (4, '연마기')
assert drill[0] == sander[0] # 무게가 같다
assert drill[1] < sander[1]  # 알파벳순으로 볼 때 더 작다
assert drill < sander        # 그러므로 드릴이 더 먼저다

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

power_tools.sort(key=lambda x: (x.weight, x.name),
                 reverse=True) # 모든 비교 기준을 내림차순으로 만든다
print(power_tools)

power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#power_tools.sort(key=lambda x: (x.weight, -x.name),
#                 reverse=True)

power_tools.sort(key=lambda x: x.name)   # name 기준 오름차순
power_tools.sort(key=lambda x: x.weight, # weight 기준 내림차순
                 reverse=True)
print(power_tools)

power_tools.sort(key=lambda x: x.name)
print(power_tools)

power_tools.sort(key=lambda x: x.weight,
                 reverse=True)
print(power_tools)
