import importlib
import pytest

import project.task1.matrices as matrices


def transposition_test():
    matrices.m = [[1, 2], [3, 4]]
    importlib.reload(matrices)
    matrices.execution_flag = True
    assert matrices.transposition_result == [[1, 3], [2, 4]]


def transposition_error_test():
    matrices.m = []
    matrices.execution_flag = True
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m = [[1], [1, 2]]
    with pytest.raises(ValueError):
        importlib.reload(matrices)


def matrix_sum_test():
    matrices.m1 = [[1, 2], [3, 4]]
    matrices.m2 = [[5, 6], [7, 8]]
    matrices.execution_flag = True
    importlib.reload(matrices)
    assert matrices.matrix_sum_result == [[6, 8], [10, 12]]


def matrix_sum_error_test():
    matrices.m1 = []
    matrices.m2 = []
    matrices.execution_flag = True
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m1 = [[1]]
    matrices.m2 = [[1, 2]]
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m1 = [[1, 2]]
    matrices.m2 = [[1]]
    with pytest.raises(ValueError):
        importlib.reload(matrices)


def matrix_multiplication_test():
    matrices.m1 = [[1, 2], [3, 4]]
    matrices.m2 = [[5, 6], [7, 8]]
    matrices.execution_flag = True
    importlib.reload(matrices)
    assert matrices.matrix_multiplication_result == [[19, 22], [43, 50]]


def matrix_multiplication_error_test():
    matrices.m1 = []
    matrices.m2 = []
    matrices.execution_flag = True
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m1 = [[1, 2]]
    matrices.m2 = [[1, 2]]
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m1 = [[1, 2, 3]]
    matrices.m2 = [[1, 2]]
    with pytest.raises(ValueError):
        importlib.reload(matrices)
