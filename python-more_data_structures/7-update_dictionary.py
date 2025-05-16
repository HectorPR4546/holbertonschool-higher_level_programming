#!/usr/bin/python3
"""Module that updates or adds a key/value in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """
    Update or add a key/value pair in the given dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to update or add.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
