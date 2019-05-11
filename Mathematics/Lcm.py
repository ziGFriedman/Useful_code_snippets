'''Возвращает наименьшее общее кратное из двух или более чисел. Используется
формула greatest common divisor (GCD) и lcm(x,y) = x * y / gcd(x,y) для определения
наименьшего общего кратного. Формула GCD использует рекурсию, а также reduce из
встроенного модуля functools.'''
from functools import reduce

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def lcm(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else _gcd(y, x % y)

    def _lcm(x, y):
        return x * y / _gcd(x, y)
    return reduce((lambda x, y: _lcm(x, y)), numbers)

print(lcm(12, 7))
print(lcm([1, 3, 4], 5))
