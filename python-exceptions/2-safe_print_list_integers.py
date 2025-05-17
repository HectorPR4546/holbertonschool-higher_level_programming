#!/usr/bin/python3
"""
This module provides a function that safely prints the first x
integers from a list.
"""

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Only integer values are printed; other types raise exceptions that
    are caught and ignored.

    Args:
        my_list (list): The list to print values from.
        x (int): Number of elements to attempt to print.

    Returns:
        int: The number of integers actually printed.
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
