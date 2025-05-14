#!/usr/bin/python3
"""Module that provides a function to delete an element at a given index."""


def delete_at(my_list=[], idx=0):
    """
    Delete an element at the specified index in a list.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to delete.

    Returns:
        list: The modified list, or the original list if index is invalid.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
