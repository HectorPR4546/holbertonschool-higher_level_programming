#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?', and ':'
"""


def text_indentation(text=None):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string or if no argument is given.
    """
    if text is None:
        raise TypeError("text_indentation() missing 1 required positional argument: 'text'")

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
