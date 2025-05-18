#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide by.

    Returns:
        list of lists: New matrix with divided values.

    Raises:
        TypeError: If matrix is not a list of lists of int/float,
                   or if rows are not of equal size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
