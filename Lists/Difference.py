'''Возвращает разницу между двумя массивами. Создает set из b и сохраняет
только те значения, которые не содержатся в b.'''
def difference(a, b):
    b = set(b)
    return [item for item in a if item not in b]

print(difference([1, 2, 3], [1, 2, 4]))
