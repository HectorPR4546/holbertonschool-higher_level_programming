#!/usr/bin/python3
"""
Module that defines an abstract base class 'Shape'
and its concrete implementations 'Circle' and 'Rectangle'.

Uses ABC to enforce the implementation of required methods in subclasses.
Demonstrates duck typing in the 'shape_info' function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class that defines the interface for shapes.
    Subclasses must implement the area() and perimeter() methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: The area value.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float: The perimeter value.
        """
        pass


class Circle(Shape):
    """
    Circle shape implementing the Shape interface.
    """

    def __init__(self, radius):
        """
        Initialize a circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: Area = π * radius^2
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: Perimeter = 2 * π * radius
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape implementing the Shape interface.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: Area = width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: Perimeter = 2 * (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape object.

    Uses duck typing: assumes the object has area() and perimeter() methods.

    Args:
        shape: Any object that implements area() and perimeter().
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
