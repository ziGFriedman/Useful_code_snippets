'''Считает количество повторений заданного значения.'''
# Используется функция reduce из встроенных модулей functools для увеличения
# счетчика каждый раз, когда вы сталкиваетесь с определенным значением внутри
# списка.
from functools import reduce

def count_occurences(arr, val):
    return reduce((lambda x, y: x + 1 if y == val and type(y) == type(val) else x + 0), arr)

print(count_occurences([1, 1, 2, 1, 2, 3], 1))
