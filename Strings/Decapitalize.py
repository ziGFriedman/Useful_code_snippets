'''Делает первую букву строки строчной, а затем добавляет ее к остальной части строки.
Параметр upper_rest опускается, чтобы сохранить остальную часть строки нетронутой,
или для нее устанавливается значение true, чтобы преобразовать в верхний регистр.'''
def decapitalize(string, upper_rest = False):
    return string[:1].lower() + (string[1:].upper() if upper_rest else string[1:])

print(decapitalize('FooBar'))
print(decapitalize('FooBar', True))
