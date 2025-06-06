#!/usr/bin/python3
"""Module to write an object to a text file using JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to serialize to JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
