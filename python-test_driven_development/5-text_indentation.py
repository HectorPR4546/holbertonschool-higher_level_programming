#!/usr/bin/python3
"""
This module defines a function that prints text with indentation.
"""

def text_indentation(text):
    """
    Prints text with two new lines after '.', '?' and ':' characters.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
