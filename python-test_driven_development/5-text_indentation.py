#!/usr/bin/python3
"""
This module provides a function that prints text
with two new lines after each '.', '?', and ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?', and ':'

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    i = 0
    length = len(text)

    while i < length:
        char = text[i]
        print(char, end='')
        if char in separators:
            print('\n')
            # Skip any spaces immediately following the separator
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
