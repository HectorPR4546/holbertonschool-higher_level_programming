#!/usr/bin/python3
"""
Module that provides a function to convert Roman numerals to integers.
"""


def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: The integer value of the Roman numeral, or 0 for invalid input.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        current_value = roman_to_int_map.get(char, 0)

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total
