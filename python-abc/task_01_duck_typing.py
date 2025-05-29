#!/usr/bin/python3
"""Abstract shape classes and duck typing demonstration."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """
        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """
        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of the shape.

    Args:
        shape: Object with area() and perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
