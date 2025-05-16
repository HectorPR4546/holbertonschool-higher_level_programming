#!/usr/bin/python3
"""
Module that provides a function to multiply all elements of a list by a number.
"""


def multiply_list_map(my_list=[], number=0):
    """
    Multiply all elements of a list by a given number using map.

    Args:
        my_list (list): A list of integers.
        number (int): The number to multiply each element by.

    Returns:
        list: A new list with all elements multiplied by the given number.
    """
    return list(map(lambda x: x * number, my_list))
