#!/usr/bin/python3
"""Module that provides a function to add two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise, filling missing values with 0s if needed.

    Args:
        tuple_a (tuple): First input tuple.
        tuple_b (tuple): Second input tuple.

    Returns:
        tuple: A new tuple with the sum of corresponding elements.
    """
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    max_len = max(len1, len2)

    padded_tuple_a = tuple_a + (0,) * (max_len - len1)
    padded_tuple_b = tuple_b + (0,) * (max_len - len2)

    result_tuple = tuple(
        x + y for x, y in zip(padded_tuple_a, padded_tuple_b)
    )
    return result_tuple
