#!/usr/bin/python3
"""Module that provides a function to replace an element in a list."""


def replace_in_list(my_list, idx, new_element):
    """
    Replace an element of a list at a specific position.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace an element.
        new_element: The new value to assign at the specified index.

    Returns:
        list: The modified list, or the original list if index is out of range.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = new_element
    return my_list
