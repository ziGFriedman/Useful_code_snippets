'''Вычисляется факториал числа.'''
# Используется рекурсия. Если num меньше или равно 1, возвращается 1, а
# иначе – произведение num и factorial из num — 1. Сработает исключение,
# если num будет отрицательным или числом с плавающей точкой.
def factorial(num):
    if not ((num >= 0) & (num % 1 == 0)):
        raise Exception("Number( {num} ) can't be floating point or negative ".format(num))
    return 1 if num == 0 else num * factorial(num - 1)

print(factorial(6))
