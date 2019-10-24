'''Выравнивание списка при помощи рекурсии. Используется list.extend() вместе с
пустым массивом (result) и функция spread для сглаживания каждого элемента списка.'''
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(arr):
    result = []
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, arr))))
    return result

print(deep_flatten([1, [2], [[3], 4, 5], 5]))
