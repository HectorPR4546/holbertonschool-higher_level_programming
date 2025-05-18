#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list): A list of lists of integers/floats.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows are of the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number and not inf/nan
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == float('inf') or div == float('-inf') or div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix
    return [[round(num / div, 2) for num in row] for row in matrix]