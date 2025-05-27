#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a function to check if an object is exactly an instance
of a given class.
"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of
    the specified class.
    """
    return type(obj) is a_class
