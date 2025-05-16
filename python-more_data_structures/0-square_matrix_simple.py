#!/usr/bin/python3
"""Module that returns a new matrix with squared values."""


def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Args:
        matrix (list of lists): A 2D list of integers.

    Returns:
        list: A new matrix with each value squared.
    """
    new_matrix = [[num ** 2 for num in row] for row in matrix]
    return new_matrix
