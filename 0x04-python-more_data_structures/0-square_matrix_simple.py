#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for row in matrix:
        empty = []
        for i in range(len(row)):
            empty.append(row[i] ** 2)
        new_matrix.append(empty)
    return new_matrix
'''
def square_matrix_simple(matrix=[]):
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

    OR

def square_matrix_simple(matrix = []):
    new_matrix = []
    for row in matrix:
        inner = []
        for num in row:
            inner.append( num ** 2)
        new_matrix.append(inner)
    return new_matrix
'''
