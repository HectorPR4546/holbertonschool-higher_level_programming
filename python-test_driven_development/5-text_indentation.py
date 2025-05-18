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

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    lines = result.split("\n")
    for line in lines:
        if line.strip() != "":
            print(line.strip())
