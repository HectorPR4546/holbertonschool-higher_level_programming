#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Main module for testing the Square class.

This script demonstrates instantiating the Square class defined in
`0-square.py` and printing its type and attributes.

Example:
    $ ./0-main.py
    <class '0-square.Square'>
    {}

Attributes:
    None

"""

Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
