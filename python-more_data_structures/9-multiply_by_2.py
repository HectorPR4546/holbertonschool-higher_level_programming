#!/usr/bin/python3
"""Module that multiplies all values in a dictionary by 2."""


def multiply_by_2(a_dictionary):
    """
    Create a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The original dictionary with integer values.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
