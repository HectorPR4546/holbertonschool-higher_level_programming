Python - Classes and Objects
Description

This project is part of the Holberton School curriculum. It introduces object-oriented programming (OOP) in Python. You will define and use classes, work with private/public attributes, add methods, and enforce data encapsulation and validation.

You will learn how to:

    Create classes and instances

    Define and access attributes

    Write methods and implement behavior

    Use the __init__ constructor and special methods like __str__

    Enforce proper documentation across modules, classes, and methods

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

Documentation Requirements

    All modules must have a docstring
    (check with: python3 -c 'print(__import__("my_module").__doc__)')

    All classes must have a docstring
    (check with: python3 -c 'print(__import__("my_module").MyClass.__doc__)')

    All functions (inside and outside classes) must have docstrings
    (check with: python3 -c 'print(__import__("my_module").my_function.__doc__)' and
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

    Documentation must be meaningful and describe the purpose and behavior accurately

Tasks

    0. My first square
    File: 0-square.py
    Defines an empty class Square.

    1. Square with size
    File: 1-square.py
    Adds a private instance attribute size.

    2. Size validation
    File: 2-square.py
    Adds validation to ensure size is an integer >= 0.

    3. Area of a square
    File: 3-square.py
    Adds a public method def area(self) that returns the square's area.

    4. Access and update private attribute
    File: 4-square.py
    Uses property decorators to get and set size with validation.

    5. Printing a square
    File: 5-square.py
    Adds a public method def my_print(self) that prints the square with #.

    6. Coordinates of a square
    File: 6-square.py
    Adds a private instance attribute position and modifies printing based on coordinates.

Usage

To run any script:

./<filename.py>

Make it executable if needed:

chmod +x <filename.py>

Author

Hector Perez - Holberton School