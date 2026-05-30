
import sys

def print_python_version():
    """Function printing python version."""
    print(sys.version)

def is_armstrong_number(number):
    number_string = str(number)
    length_of_number = len(number_string)
    total = 0
    for digit in number_string:
        digit = int(digit)
        digit = digit ** length_of_number
        total += digit

    return total == int(number)