#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a function to check if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
