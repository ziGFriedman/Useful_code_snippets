'''Возвращает среднее от двух и более чисел. Происходит деление на len(args) суммы
всех элементов args.'''
def average(*args):
    return sum(args) / len(args)

print(average(*[1, 2, 3]))
print(average(7, 2, 3))
