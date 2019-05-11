'''Возвращает True если строка является палиндромом, иначе False.'''
# Преобразует строку str.lower() и использует re.sub  для удаления не
# алфавитно-цифровых символов. Потом сравнивает новую строку с реверсивной строкой.
def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]

print(palindrome('taco cat'))
