#!/usr/bin/python3
"""Module that defines a function to print integers from a list."""


def print_list_integer(my_list=[]):
    """
    Print all integers in a list, one per line.

    Args:
        my_list (list): A list of integers to be printed.
    """
    for number in my_list:
        print("{:d}".format(number))
