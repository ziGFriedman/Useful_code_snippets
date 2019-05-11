'''Вычисляется наибольший общий делитель между двумя или более числами / списками.'''
# В helperGcdfunction используется рекурсия. Базовый случай, когда y равно 0. В
# этом случае возвращается x. В противном случае возвращается y и остаток от
# деления x/y. Используется reduce из встроенного модуля functools.
from functools import reduce

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def gcd(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else gcd(y, x % y)
    return reduce((lambda x, y: _gcd(x, y)), numbers)

print(gcd(8, 36, 80))
