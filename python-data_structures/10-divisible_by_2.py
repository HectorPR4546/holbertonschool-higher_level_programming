#!/usr/bin/python3
"""Module that checks which elements in a list are divisible by 2."""


def divisible_by_2(my_list=[]):
    """
    Return a list of booleans indicating if elements are divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of booleans where True means the element at that index
        is divisible by 2.
    """
    divisible = []
    for num in my_list:
        divisible.append(num % 2 == 0)
    return divisible
