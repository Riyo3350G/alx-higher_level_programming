#!/usr/bin/python3
"""pascale_triangle module"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev_row = triangle[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
