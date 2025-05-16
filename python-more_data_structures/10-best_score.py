#!/usr/bin/python3
"""Module that returns the key with the highest value in a dictionary."""


def best_score(a_dictionary):
    """
    Return the key with the highest integer value in the dictionary.

    Args:
        a_dictionary (dict): The dictionary containing integer scores.

    Returns:
        str: The key with the highest score, or None if the dictionary is empty or None.
    """
    if not a_dictionary:
        return None

    max_key = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
