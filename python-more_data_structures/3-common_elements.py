#!/usr/bin/python3
"""Module that finds common elements in two sets."""


def common_elements(set_1, set_2):
    """
    Return a set of elements common to both set_1 and set_2.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the common elements.
    """
    common_set = set()
    for element in set_1:
        if element in set_2:
            common_set.add(element)
    return common_set
