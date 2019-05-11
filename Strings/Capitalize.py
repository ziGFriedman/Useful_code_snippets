'''Делает первую букву строки заглавной.'''
# Делает первую букву строки заглавной, а затем добавляет ее к остальной части строки.
# Параметр lower_rest опускается, чтобы сохранить остальную часть строки нетронутой,
# или для нее устанавливается значение true, чтобы преобразовать в нижний регистр.
def capitalize(string, lower_rest = False):
    return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])

print(capitalize('fooBar'))
print(capitalize('fooBar', True))
