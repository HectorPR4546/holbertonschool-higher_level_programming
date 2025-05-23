#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a Rectangle class.

This module provides a class Rectangle with width and height attributes.
It includes validation, methods to compute area, perimeter, a string
representation using the `print_symbol`, and cleanup message on deletion.
"""


class Rectangle:
    """Represents a rectangle defined by its width and height."""

    number_of_instances = 0
    print_symbol = '#'  # Symbol for rectangle string representation

    @classmethod
    def square(cls, size=0):
        """Creates a square Rectangle instance."""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles by their area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.

        Returns:
            Rectangle: The bigger rectangle or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): Width of rectangle (default 0).
            height (int): Height of rectangle (default 0).
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Width of the rectangle.

        Raises:
            TypeError: If width is not an int.
            ValueError: If width < 0.
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
        """int: Height of the rectangle.

        Raises:
            TypeError: If height is not an int.
            ValueError: If height < 0.
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
        """Compute the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Compute the perimeter of the rectangle.

        Returns:
            int: Perimeter, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Informal string representation with `print_symbol`.

        Returns:
            str: Rectangle represented by lines of `print_symbol`.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append(str(self.print_symbol) * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """Official string representation.

        Returns:
            str: String to recreate the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message on instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
