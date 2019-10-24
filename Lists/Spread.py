'''Заимствует [].concat(…arr) из Javascript. Сглаживает список (не глубоко) и
возвращает новый список.'''
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

print(spread([1,2,3,[4,5,6],[7, 8],8,9]))
