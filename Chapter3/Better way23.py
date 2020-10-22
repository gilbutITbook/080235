
#
# 아이템 23
#

def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

#
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#remainder(number=20, 7)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#remainder(20, number=7)

#
my_kwargs = {
    'number': 20,
    'divisor': 7,
}

assert remainder(**my_kwargs) == 6

#
my_kwargs = {
    'divisor': 7,
}

assert remainder(number=20, **my_kwargs) == 6

#
my_kwargs = {
    'number': 20,
}

other_kwargs = {
    'divisor': 7,
}

assert remainder(**my_kwargs, **other_kwargs) == 6

#
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, 감마=4)

#
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg/s')

#
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff, 1)

#
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)

#
def flow_rate(weight_diff, time_diff,
              period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, units_per_kg=2.2)

pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
