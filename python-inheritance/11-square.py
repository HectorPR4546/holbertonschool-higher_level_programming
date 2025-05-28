#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a square with a given size.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square.

        Returns:
            str: Formatted string as [Square] size/size
        """
        return f"[Square] {self.__size}/{self.__size}"
