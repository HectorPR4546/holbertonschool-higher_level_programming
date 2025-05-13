#!/usr/bin/python3
"""Module that provides a function to create a modified copy of a list."""


def new_in_list(my_list, idx, new_element):
    """
    Replace an element in a list at a given index without modifying
    the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        new_element: The new value to insert at the given index.

    Returns:
        list: A new list with the modified element, or the original list
        if the index is out of range.
    """
    if 0 <= idx < len(my_list):
        new_list = my_list[:]
        new_list[idx] = new_element
        return new_list
    else:
        return my_list
