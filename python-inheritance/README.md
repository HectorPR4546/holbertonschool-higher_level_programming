Python - Inheritance
Description

This project introduces the concept of inheritance in object-oriented programming using Python. It covers class relationships, method overriding, attribute inheritance, and the usage of built-in functions related to class hierarchies.
Learning Objectives

By the end of this project, you should be able to explain:

    What is a superclass, base class, or parent class

    What is a subclass

    How to list all attributes and methods of a class or instance

    When can an instance have new attributes

    How to inherit a class from another

    How to define a class with multiple base classes

    What is the default class every class inherits from

    How to override a method or attribute inherited from the base class

    Which attributes or methods are inherited by subclasses

    What is the purpose of inheritance

    When and how to use isinstance(), issubclass(), type(), and super()

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs

    Files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5

    All files must end with a new line

    The first line of all files must be exactly #!/usr/bin/python3

    A README.md file is mandatory

    Code must follow pycodestyle (version 2.7.*)

    All files must be executable

    File lengths will be tested using wc

Python Test Cases

    Allowed editors: vi, vim, emacs

    All test files must end with a new line

    Test files must be inside a tests folder

    Test files must have .txt extension

    Tests executed using: python3 -m doctest ./tests/*

    All modules, classes, and functions must have proper documentation

    Documentation must be meaningful sentences explaining the purpose

    Avoid using import or from in comments

Tasks

    0. Lookup
    File: 0-lookup.py
    Function that returns the list of available attributes and methods of an object.

    1. My list
    File: 1-my_list.py
    Class MyList that inherits from list and prints a sorted list.

    2. Exact same object
    File: 2-is_same_class.py
    Function that returns True if object is exactly an instance of specified class.

    3. Same class or inherit from
    File: 3-is_kind_of_class.py
    Function that returns True if object is an instance of, or inherits from, a specified class.

    4. Only sub class of
    File: 4-inherits_from.py
    Function that returns True if object inherits (directly or indirectly) from the specified class.

    5. Geometry module
    File: 5-base_geometry.py
    Empty class BaseGeometry.

    6. Improve Geometry
    File: 6-base_geometry.py
    Class BaseGeometry with a public instance method area() that raises Exception.

    7. Integer validator
    File: 7-base_geometry.py
    Adds integer_validator() method to BaseGeometry.

    8. Rectangle
    File: 8-rectangle.py
    Class Rectangle that inherits from BaseGeometry and validates width and height.

    9. Full rectangle
    File: 9-rectangle.py
    Adds area() and __str__() methods to Rectangle.

    10. Square #1
    File: 10-square.py
    Class Square that inherits from Rectangle.

    11. Square #2
    File: 11-square.py
    Adds area() and __str__() to Square.

Usage

Make any script executable:

chmod +x <filename.py>

Run the script:

./<filename.py>

Run tests:

python3 -m doctest ./tests/*

Author

Hector Perez - Holberton School