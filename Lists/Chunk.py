'''Разбиение массива на меньшие списки указанного размера. Для создания списка
желаемого размера используется range, а заполняется список при помощи map.'''
from math import ceil

def chunk(arr, size):
    return list(map(lambda x: arr[x * size:x * size + size], list(range(0, ceil(len(arr) / size)))))

print(chunk([1,2,3,4,5], 2))
