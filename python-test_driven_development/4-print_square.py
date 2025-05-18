#!/usr/bin/python3
"""Function that prints a square with the character #."""

def print_square(size):
    """
    Prints a square of size 'size' using the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    if size is None:
        raise TypeError(err)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
