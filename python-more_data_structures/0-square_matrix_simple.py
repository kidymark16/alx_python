#!/usr/bin/python3
"""
This module contains a function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    # Fill in the new matrix with the square values of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    return result
