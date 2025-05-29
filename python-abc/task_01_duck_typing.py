#!/usr/bin/env python3
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.
    Defines abstract methods for area and perimeter.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Concrete class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a Circle object with a given radius.
        Args:
            radius (float or int): The radius of the circle.
        """
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.
        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Concrete class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with a given width and height.
        Args:
            width (float or int): The width of the rectangle.
            height (float or int): The height of the rectangle.
        """
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a non-negative number.")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a non-negative number.")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    Relies on duck typing, assuming the 'shape' object has
    'area' and 'perimeter' methods.
    Args:
        shape: An object that behaves like a Shape (has area and perimeter methods).
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
