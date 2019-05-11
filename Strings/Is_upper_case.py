'''Преобразует строку в нижний регистр при помощи метода str.upper() и сравнивает ее с оригиналом.'''
def is_upper_case(str):
    return str == str.upper()

print(is_upper_case('ABC'))
print(is_upper_case('a3@$'))
print(is_upper_case('aB4'))
