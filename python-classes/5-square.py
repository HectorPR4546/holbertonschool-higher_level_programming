#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a class Square.

This module provides the Square class which represents a square with a
size and position. It includes validation for its attributes, a method
to compute the area, and a method to print the square.
"""


class Square:
    """Represents a square.

    This class defines a square with private size and position attributes,
    and provides methods to calculate area and print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The position of the square (x, y) offset."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the `#` character, using position offset."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
