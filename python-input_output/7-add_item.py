#!/usr/bin/python3
"""Adds all command-line arguments to a Python list and saves them to a JSON file.

This script loads existing items from 'add_item.json', adds new arguments,
and saves the updated list back to the file.
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    """Main function that handles the list operations."""
    filename = "add_item.json"
    
    # Load existing items or start with empty list
    if path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []
    
    # Add new arguments and save
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
