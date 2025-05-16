#!/usr/bin/python3
"""Module that returns the symmetric difference of two sets."""


def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements present in only one of the two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing elements that are in either set_1 or set_2,
             but not in both.
    """
    diff_set = set()

    for element in set_1:
        if element not in set_2:
            diff_set.add(element)

    for element in set_2:
        if element not in set_1:
            diff_set.add(element)

    return diff_set
