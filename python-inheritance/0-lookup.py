#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a function for retrieving attributes and methods of an object."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of attribute and method names (as strings).
    """
    return dir(obj)
