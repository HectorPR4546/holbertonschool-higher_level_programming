#!/usr/bin/python3
"""Module that provides a function to remove all 'c' and 'C' characters."""


def no_c(input_string):
    """
    Return a new string with all 'c' and 'C' characters removed.

    Args:
        input_string (str): The original string.

    Returns:
        str: A new string without any 'c' or 'C' characters.
    """
    new_string = ""
    for char in input_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
