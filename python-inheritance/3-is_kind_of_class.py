#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Checks if an object is an instance or inherits from a class."""


def is_kind_of_class(obj, a_class):
    """Determines if obj is an instance of a_class or its subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance or subclass instance of a_class.
    """
    return isinstance(obj, a_class)
