#!/usr/bin/python3
# -*- coding: utf-8 -*-
def integer_validator(self, name, value):
    """Validates that a parameter is a positive integer.

    Args:
        name (str): The name of the parameter.
        value (int): The value to validate.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is not greater than 0.
    """
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")
