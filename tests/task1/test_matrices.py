import importlib
import pytest

import project.task1.matrices as matrices


def test_transposition():
    matrices.m = [[1, 2], [3, 4]]
    importlib.reload(matrices)
    assert matrices.transposition_result == [[1, 3], [2, 4]]


def test_transposition_error():
    matrices.m = []
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m = [[1], [1, 2]]
    with pytest.raises(ValueError):
        importlib.reload(matrices)

    matrices.m = [[1]]


def test_matrix_sum():
    matrices.m1 = [[1, 2], [3, 4]]
    matrices.m2 = [[5, 6], [7, 8]]
    importlib.reload(matrices)
    assert matrices.matrix_sum_result == [[6, 8], [10, 12]]


def test_matrix_sum_error():
    matrices.m1 = []
    matrices.m2 = []
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

    matrices.m1 = [[1]]
    matrices.m2 = [[1]]


def test_matrix_multiplication():
    matrices.m1 = [[1, 2], [3, 4]]
    matrices.m2 = [[5, 6], [7, 8]]
    importlib.reload(matrices)
    assert matrices.matrix_multiplication_result == [[19, 22], [43, 50]]


def test_matrix_multiplication_error():
    matrices.m1 = []
    matrices.m2 = []
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

    matrices.m1 = [[1]]
    matrices.m2 = [[1]]
