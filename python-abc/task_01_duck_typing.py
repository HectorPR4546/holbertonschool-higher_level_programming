#!/usr/bin/python3
"""
Module that defines an abstract base class 'Shape'
and its concrete implementations 'Circle' and 'Rectangle'.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class that defines the interface for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape implementing the Shape interface.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape implementing the Shape interface.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape object.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    shape_info(circle)
    shape_info(rectangle)
