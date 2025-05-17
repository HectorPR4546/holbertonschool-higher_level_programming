Python - Test-driven development
Description

This project is part of the Holberton School curriculum. It introduces the concept of Test-Driven Development (TDD) in Python, emphasizing writing tests before the implementation. You’ll also learn how to use doctests and unittest modules to create comprehensive and effective test cases.

You will practice:

    Writing documentation for functions and modules

    Creating test cases with doctest and unittest

    Validating correctness, edge cases, and input validation

    Structuring projects using tests as the backbone of development

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs

    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5

    All your files should end with a new line

    The first line of all your files should be exactly #!/usr/bin/python3

    A README.md file at the root of the project folder is mandatory

    Your code should follow pycodestyle (version 2.7.*)

    All your files must be executable

    File lengths will be tested using wc

Python Test Cases

    Allowed editors: vi, vim, emacs

    All test files must end with a new line

    All test files should be in a folder named tests

    All test files should be plain text files with a .txt extension

    Tests should be executed using:

    python3 -m doctest ./tests/*

    All modules must have a full documentation string
    (check with: python3 -c 'print(__import__("my_module").__doc__)')

    All functions must also have a full documentation string
    (check with: python3 -c 'print(__import__("my_module").my_function.__doc__)')

    Documentation must be a real sentence explaining the purpose of the module/class/function

    It is highly encouraged to collaborate with peers when writing test cases to cover all possible scenarios

Tasks

    0. Integers addition
    File: 0-add_integer.py
    Adds two integers with input validation and doctests.

    1. Divide a matrix
    File: 2-matrix_divided.py
    Divides all elements of a matrix by a number, with detailed error handling and doctests.

    2. Say my name
    File: 3-say_my_name.py
    Prints a simple sentence using first and last name, with validation and doctests.

    3. Print square
    File: 4-print_square.py
    Prints a square with the character #, using input validation and doctests.

    4. Text indentation
    File: 5-text_indentation.py
    Prints indented text following certain punctuation rules, with thorough testing.

    5. Max integer - Unittest
    File: 6-max_integer_test.py
    Uses the unittest module to test a function that returns the max integer in a list.

Usage

To run any Python script:

./<filename.py>

Make it executable if needed:

chmod +x <filename.py>

To run doctests:

python3 -m doctest ./tests/*

To run unittests:

python3 -m unittest 6-max_integer_test.py

Author

Hector Perez - Holberton School