#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a class Square.

This module provides the Square class which represents a square.
The class includes initialization with size validation, a method
to compute the area, and getter/setter for size.
"""


class Square:
    """Represents a square.

    This class defines a square with a private size attribute and provides
    a method to compute its area, along with property access to size.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """int: Gets or sets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
