#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a Rectangle class.

This module provides a class Rectangle with attributes for width and height.
It includes validation, and methods to compute area, perimeter, a string
representation using the `#` character, and cleanup message on deletion.
"""


class Rectangle:
    """Represents a rectangle defined by its width and height."""

    number_of_instances = 0  # <-- Class variable to track instances

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Provides an informal string representation of the rectangle.

        Returns:
            str: A string made of '#' characters forming the shape of the
            rectangle, or an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """Provides an official string representation of the rectangle.

        Returns:
            str: A string that can recreate the rectangle using eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
