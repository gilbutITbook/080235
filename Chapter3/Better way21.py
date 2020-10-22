
#
# 아이템 21
#
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

#
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True # 문제를 쉽게 해결할 수 있을 것 같다
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('발견:', found)
print(numbers)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#foo = does_not_exist * 5

#
def sort_priority2(numbers, group):
    found = False  # 영역: 'sort_priority2'
    def helper(x):
        if x in group:
            found = True  # 영역: 'helper' -- 좋지 않음!
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

#
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        nonlocal found       # 추가함
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

#
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
