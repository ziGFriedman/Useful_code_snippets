'''Преобразует строку в верхний регистр при помощи метода str.lower() и сравнивает ее с оригиналом.'''
def is_lower_case(str):
    return str == str.lower()

print(is_lower_case('abc'))
print(is_lower_case('a3@$'))
print(is_lower_case('Ab4'))
