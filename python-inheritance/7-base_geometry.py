#!/usr/bin/python3
"""Defines a base geometry class with validation methods."""


class BaseGeometry:
    """Represents base geometric operations and validations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Indicates area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
