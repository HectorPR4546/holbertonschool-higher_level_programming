#!/usr/bin/python3
"""Module defining abstract Shape class and its implementations."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
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
    Print area and perimeter of a shape.

    Args:
        shape: Object with area() and perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
