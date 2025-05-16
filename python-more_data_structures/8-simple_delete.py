#!/usr/bin/python3
"""Module that deletes a key from a dictionary."""


def simple_delete(a_dictionary, key=""):
    """
    Delete a key from the given dictionary, if it exists.

    Args:
        a_dictionary (dict): The dictionary from which to delete the key.
        key (str): The key to delete.

    Returns:
        dict: The dictionary after deletion.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
