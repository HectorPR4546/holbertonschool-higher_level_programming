#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Each row is printed on a new line with elements separated by spaces.

    Args:
        matrix (list of lists): The matrix to print.
    """
    for row in matrix:
        print(' '.join("{:d}".format(num) for num in row))
