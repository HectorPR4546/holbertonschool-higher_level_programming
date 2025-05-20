#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a class Square.

This module provides the Square class which represents a square.
The class is initialized with a size and stores it as a private attribute.
"""


class Square:
    """Represents a square.

    This class defines a square with a private size attribute.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
