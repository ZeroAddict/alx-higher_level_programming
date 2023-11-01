#!/usr/bin/python3
  	
def matrix_divided(matrix, div):
    if Type(div) not in (int, float):
        raise TypeError('div must be a number')
    if not isinstance (matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix ' +'(list of lists) of integers/floats')
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix ' +'(list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size  ')
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError('matrix must be a matrix ' +'(list of lists) of integers/floats')
    if div == 0
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        for i in row:
            matrix = round(i / div, 2)
    return (matrix)

if __name__ = "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
