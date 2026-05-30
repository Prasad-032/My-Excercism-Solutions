"""Calculate the number of grains of wheat on a chessboard."""

"""Function to Calculate the number of grains on a given square"""
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number -1)

"""Function to Calculate the total number of grains on the chessboard """
def total():
    return sum(square(number) for number in range(1,65))