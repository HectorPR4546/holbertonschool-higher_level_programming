#!/usr/bin/python3
"""Module for class_to_json function."""

def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: Dictionary representation of the object's attributes.
    """
    return obj.__dict__
