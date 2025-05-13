#!/usr/bin/python3
"""Module that provides a function to return string length and first char."""


def multiple_returns(sentence):
    """
    Return the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the string and its first
        character, or None if the string is empty.
    """
    return (len(sentence), sentence[0] if sentence else None)
