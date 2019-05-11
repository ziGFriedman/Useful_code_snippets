'''Возвращает number гласных в string. При помощи регулярного выражения,
вычисляется количество гласных (A, E, I, O, U) в строке.'''
import re

def count_vowels(str):
    return len(re.findall(r'[aeiouy]', str, re.IGNORECASE))

print(count_vowels('foobar'))
print(count_vowels('gym'))
