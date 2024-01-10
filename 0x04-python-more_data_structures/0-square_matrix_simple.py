i#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for row in matrix:
        empty = []
        for i in range(len(row)):
            empty.append(row[i] ** 2)
        new_matrix.append(empty)
    return new_matrix
