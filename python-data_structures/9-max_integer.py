#!/usr/bin/python3
"""Module that provides a function to find the max integer in a list."""


def max_integer(my_list=[]):
    """
    Return the largest integer in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        int or None: The maximum integer in the list, or None if the list
        is empty.
    """
    if not my_list:
        return None

    max_value = my_list[0]
    for number in my_list:
        if number > max_value:
            max_value = number
    return max_value
