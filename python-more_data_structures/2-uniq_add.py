#!/usr/bin/python3
"""Module that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """
    Add all unique integers in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        int: Sum of all unique integers in the list.
    """
    total = 0
    new_list = []
    for num in my_list:
        if num not in new_list:
            new_list.append(num)
            total += num
    return total
