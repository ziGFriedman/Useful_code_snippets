'''Создает список элементов, группируя их на основании позиции в оригинальном списке.
Используется max вместе с list comprehension для получения длины самого длинного
списка в аргументах. В качестве длины lists используется значение fill_value.
По умолчанию значение fill_value равно None.'''

def zip(*args):
    max_length = max([len(arr) for arr in args])
    result = []
    for i in range(max_length):
        result.append([args[k][i] if i < len(args[k]) else None for k in range(len(args))])
    return result

print(zip(['a', 'b'], [1, 2], [True, False]))
print(zip(['a'], [1, 2], [True, False]))
print(zip(['a'], [1, 2], [True, False]))
