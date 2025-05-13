#!/usr/bin/python3
"""Module that provides a function to retrieve an element from a list."""


def element_at(my_list, idx):
    """
    Retrieve an element from a list at a given index.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index, or None if index is out of range.
    """
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
