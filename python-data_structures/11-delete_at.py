#!/usr/bin/python3
"""Module that provides a function to delete an item from a list."""


def delete_at(my_list=[], idx=0):
    """
    Delete an element at a specific index in a list.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to delete.

    Returns:
        list: The modified list after deletion, or original if index is
        out of range or invalid.
    """
    if not isinstance(my_list, list):
        print("Error: Input must be a list.")
        return my_list

    if not isinstance(idx, int):
        print("Error: Position must be an integer.")
        return my_list

    if idx < 0 or idx >= len(my_list):
        print("Error: Position is out of range.")
        return my_list

    del my_list[idx]
    return my_list
