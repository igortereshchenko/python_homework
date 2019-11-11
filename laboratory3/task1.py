""""
тут написати завдання=>
Написати програму, що збільшує Х на 1
"""

"""
тут написати переформульоване завдання, 
де враховуються усі  змінні=>
Написати програму, що додає два числа
"""

from validators.validators_library import validator
from validators.validators_library import re_float




def sum(a, b):
    """
    This fucntion add two floats

    Args:
        a:   float number
        b:   float number


    Returns:
        A float number is the result.

    Examples:
        >>> print(sum(11.5,0.5))
        12.0

    """


    return a + b


number1 = float (validator(re_float,'Enter first number: '))
number2 = float (validator(re_float,'Enter second number: '))

print(sum(number1,number2))

