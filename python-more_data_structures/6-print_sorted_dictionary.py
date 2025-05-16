#!/usr/bin/python3
"""Module that prints a dictionary with keys sorted."""


def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary with keys sorted in alphabetical order.

    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
