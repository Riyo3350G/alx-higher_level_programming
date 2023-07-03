#!/usr/bin/python3
"""
    Prints square
"""


def print_square(size):
    """
    Function thats Prints squares
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            print("#", end="")
        print()
