#!/usr/bin/python3
"""
This module defines a function that safely prints the first x
integers in a list.

Only integers are printed. Other types are ignored.
"""

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): Number of elements to attempt to print.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
