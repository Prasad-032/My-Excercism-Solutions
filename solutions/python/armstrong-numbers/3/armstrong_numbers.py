"""Check whether a number is an Armstrong number."""

import sys

def print_python_version():
    """Function printing python version."""
    print(sys.version)

def is_armstrong_number(number):
    """To Determine whether a number is an Armstrong number"""
    number_string = str(number)
    length_of_number = len(number_string)
    total = 0
    for digit in number_string:
        digit_number = int(digit)
        digit_number = digit_number ** length_of_number
        total += digit_number

    return total == int(number)