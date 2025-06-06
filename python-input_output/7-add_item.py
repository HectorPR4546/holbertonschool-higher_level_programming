#!/usr/bin/python3
"""Module for adding command line arguments to a JSON file.

This script maintains a persistent list in 'add_item.json' that accumulates
all arguments passed during multiple executions. It demonstrates basic
file I/O operations with JSON serialization.
"""

import os
import sys
saveJ = __import__('5-save_to_json_file').save_to_json_file
loadJ = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.exists(filename):
    items = loadJ(filename)
else:
    items = []

items.extend(sys.argv[1:])
saveJ(items, filename)
