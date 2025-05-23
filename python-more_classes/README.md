Python - More Classes and Objects
Description

This project continues the exploration of Object-Oriented Programming (OOP) in Python. It focuses on classes, attributes, methods, encapsulation, special methods, and dynamic behavior of objects and instances.
Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly and confidently:

    Why Python programming is awesome

    What is OOP (Object-Oriented Programming)

    What “first-class everything” means

    What is a class

    What is an object and an instance

    The difference between a class and an object/instance

    What is an attribute

    How to use public, protected, and private attributes

    What is self and how it is used

    What is a method

    What is the __init__ method and how to use it

    What is data abstraction, data encapsulation, and information hiding

    What is a property and how it differs from an attribute

    Pythonic ways to write getters and setters

    What are the special methods __str__ and __repr__

    The difference between __str__ and __repr__

    What is a class attribute vs. an instance attribute

    What is a class method

    What is a static method

    How to dynamically add new attributes to instances

    How to bind attributes to objects and classes

    The purpose of __dict__ for classes and instances

    How Python finds attributes of an object or class

    How to use the built-in getattr() function

Requirements
General

    Allowed editors: vi, vim, emacs

    All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5

    All files should end with a new line

    The first line of all Python files must be exactly #!/usr/bin/python3

    A README.md file at the root of the project folder is mandatory

    Code should follow pycodestyle (version 2.7.*)

    All files must be executable

    File lengths will be tested using wc

Tasks

    0. Simple rectangle
    File: 0-rectangle.py
    Defines an empty class Rectangle.

    1. Real definition of a rectangle
    File: 1-rectangle.py
    Adds width and height attributes with validation.

    2. Area and Perimeter
    File: 2-rectangle.py
    Adds public methods area() and perimeter().

    3. String representation
    File: 3-rectangle.py
    Defines the __str__ method to print the rectangle with #.

    4. Eval is magic
    File: 4-rectangle.py
    Adds __repr__ method for recreating the instance with eval().

    5. Detect instance deletion
    File: 5-rectangle.py
    Defines __del__ to print a message when an instance is deleted.

    6. How many instances
    File: 6-rectangle.py
    Adds a class attribute to count the number of instances.

    7. Change representation
    File: 7-rectangle.py
    Adds a class attribute to change the print symbol.

    8. Compare rectangles
    File: 8-rectangle.py
    Adds a static method bigger_or_equal() to compare rectangles.

    9. A square is a rectangle
    File: 9-rectangle.py
    Adds a class method square() that returns a new Rectangle with equal sides.

Usage

To run any script:

./<filename.py>

Make it executable if needed:

chmod +x <filename.py>

Author

Hector Perez - Holberton School