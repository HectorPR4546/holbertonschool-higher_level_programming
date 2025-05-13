#!/usr/bin/python3
"""Module that defines a function to print a list of integers in reverse."""


def print_reversed_list_integer(my_list=[]):
    """
    Print all integers in a list in reverse order, one per line.

    Args:
        my_list (list): A list of integers to be printed in reverse.
    """
    for number in reversed(my_list):
        print("{:d}".format(number))
