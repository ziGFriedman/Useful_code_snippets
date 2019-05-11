'''Возвращает n максимальных элементов из списка. Если n больше или равно длине
списка, возвращается исходный список, отсортированный в порядке убывания.'''

from copy import deepcopy

def max_n(arr, n = 1):
    numbers = deepcopy(arr)
    numbers.sort()
    numbers.reverse()
    return numbers[:n]

print(max_n([1, 2, 3]))
print(max_n([1, 2, 3], 2))
