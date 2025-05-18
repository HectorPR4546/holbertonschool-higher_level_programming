#!/usr/bin/python3
"""
This module defines the matrix_divided function
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix

    Args:
        matrix (list of lists): Matrix to divide
        div (int or float): Number to divide by

    Returns:
        list of lists: New matrix with divided values, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats
        TypeError: If rows are not all the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
