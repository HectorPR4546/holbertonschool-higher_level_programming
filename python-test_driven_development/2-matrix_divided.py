#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimals.
    
    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor.
    
    Returns:
        new matrix with all elements divided by div.
    
    Raises:
        TypeError: if matrix or div invalid.
        ZeroDivisionError: if div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == float('-inf'):
        # Division by infinity: all results 0.0
        return [[0.0 for _ in row] for row in matrix]

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Divide and round
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
