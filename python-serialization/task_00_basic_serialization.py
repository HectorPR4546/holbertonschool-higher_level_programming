#!/usr/bin/env python3
"""Basic serialization module that converts dictionary to JSON file and back."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): File to save the JSON data to (will overwrite)
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Deserialize JSON file to recreate Python dictionary.
    
    Args:
        filename (str): JSON file to load
        
    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, 'r') as f:
        return json.load(f)
