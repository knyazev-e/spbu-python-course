import pytest

from project.task1.matrices import transpose, matrix_sum, matrix_multiplication


def transposition_test():
    m = [[1, 2], [3, 4]]
    assert transpose(m) == [[1, 3], [2, 4]]


def transposition_error_test():
    with pytest.raises(ValueError):
        transpose([])
    with pytest.raises(ValueError):
        transpose([[1], [1, 2]])


def matrix_sum_test():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    assert matrix_sum(m1, m2) == [[6, 8], [10, 12]]


def matrix_sum_error_test():
    with pytest.raises(ValueError):
        matrix_sum([], [])
    with pytest.raises(ValueError):
        matrix_sum([[1]], [[1, 2]])
    with pytest.raises(ValueError):
        matrix_sum([[1, 2]], [[1]])


def matrix_multiplication_test():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    assert matrix_multiplication(m1, m2) == [[19, 22], [43, 50]]


def matrix_multiplication_error_test():
    with pytest.raises(ValueError):
        matrix_multiplication([], [])
    with pytest.raises(ValueError):
        matrix_multiplication([[1, 2]], [[1, 2]])
    with pytest.raises(ValueError):
        matrix_multiplication([[1, 2, 3]], [[1, 2]])
