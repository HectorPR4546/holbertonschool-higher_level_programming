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

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div != div or div == float("inf") or div == float("-inf"):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(elem / div, 2) for elem in row] for row in matrix]
