#!/usr/bin/env python3
"""Rotates a square matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a square matrix
    Args:
        matrix: nxn matrix
    Returns:
        90 degree rotated matrix
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
