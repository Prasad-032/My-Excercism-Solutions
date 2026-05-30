
def is_armstrong_number(number):
    """To Determine whether a number is an Armstrong number"""
    total = sum( [int(digit) ** len(str(number)) for digit in str(number)])
    return total == number