#!/usr/bin/python3
"""
This module provides a function that prints a text
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

    separators = {'.', '?', ':'}
    i = 0
    length = len(text)
    start_of_line = True

    while i < length:
        char = text[i]

        if start_of_line and char == ' ':
            i += 1
            continue

        print(char, end='')

        if char in separators:
            print('\n')
            print()
            start_of_line = True
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue

        start_of_line = False
        i += 1
