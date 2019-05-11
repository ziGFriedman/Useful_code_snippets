'''Возвращает разницу между двумя списками, после применения функции к обоим спискам.
Создает set, применяя fn к каждому элементу в b, затем использует сочетание fn и a,
чтобы сохранить только значения, не содержащиеся в ранее созданном set.'''
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]

from math import floor
print(difference_by([2.1, 1.2], [2.3, 3.4], floor))
print(difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']))
