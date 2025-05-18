#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    result = ""

    while i < length:
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    # Split and strip lines to avoid leading/trailing spaces
    lines = result.split('\n')
    non_empty_lines = [line.strip() for line in lines if line.strip() != ""]

    # If text contains none of the punctuation, print it as is without extra newline
    if all(punct not in text for punct in ".?:"):
        print(text, end="")
    else:
        for line in non_empty_lines:
            print(line)
