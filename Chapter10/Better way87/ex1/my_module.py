# my_module.py
def determine_weight(volume, density):
    if density <= 0:
        raise ValueError('밀도는 0보다 커야 합니다')
    ...
