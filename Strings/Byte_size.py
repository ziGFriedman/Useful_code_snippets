'''Возвращает длину строки в байтах. Заданная строка кодируется utf-8, а потом
находится ее длина.'''
def byte_size(string):
    return(len(string.encode('utf-8')))

print(byte_size('😀'))
print(byte_size('Hello World'))
