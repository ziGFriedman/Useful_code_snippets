'''Удаление ложных значений (False, None, 0, и «») из списка при помощи filter().'''
def compact(arr):
    return list(filter(lambda x: bool(x), arr))

print(compact([0, 1, False, 2, '', 3, 'a', 's', 34]))
