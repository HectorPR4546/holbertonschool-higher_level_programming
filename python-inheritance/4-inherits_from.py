#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a function that checks inheritance relationships."""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass (but not the same class) of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        but not a direct instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
