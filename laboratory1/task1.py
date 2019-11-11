"""
тут написати завдання=>
Написати програму, що додає два цілих числа більших за 0
"""

import re

re_integer = re.compile("^[-+]{0,1}\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_greater_zero_validator(prompt):

    number = int(validator(re_integer, prompt))
    while number<=0:
        number = int(validator(re_integer, prompt))

    return number

number1 =  int_greater_zero_validator('Enter first integer > 0: ')
number2 =  int_greater_zero_validator('Enter second integer > 0 : ')


print(number1+number2)









