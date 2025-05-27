#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a class BaseGeometry with validation methods."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception since area is not implemented.

        Raises:
            Exception: Always raised with the message that area is
            not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
