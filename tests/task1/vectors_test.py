import importlib
import math
import pytest

import project.task1.vectors as vectors


def scalar_multiplication_test():
    vectors.v1 = [1, 2, 3]
    vectors.v2 = [4, 5, 6]
    vectors.execution_flag = True
    importlib.reload(vectors)
    assert vectors.scalar_multiplication_result == 32


def scalar_multiplication_error_test():
    vectors.v1 = [1, 2]
    vectors.v2 = [1]
    vectors.execution_flag = True
    with pytest.raises(ValueError):
        importlib.reload(vectors)


def vector_sum_test():
    vectors.v1 = [1, 2, 3]
    vectors.v2 = [4, 5, 6]
    vectors.execution_flag = True
    importlib.reload(vectors)
    assert vectors.vector_sum_result == [5, 7, 9]


def vector_sum_error_test():
    vectors.v1 = [1, 2]
    vectors.v2 = [1]
    vectors.execution_flag = True
    with pytest.raises(ValueError):
        importlib.reload(vectors)


def length_test():
    vectors.v = [3, 4]
    vectors.execution_flag = True
    importlib.reload(vectors)
    assert math.isclose(vectors.length, 5.0)
    vectors.v = []
    importlib.reload(vectors)
    assert vectors.length == 0.0


def angle_calculation_test():
    vectors.v1 = [1, 0]
    vectors.v2 = [0, 1]
    vectors.execution_flag = True
    importlib.reload(vectors)
    assert math.isclose(vectors.angle, math.pi / 2)


def angle_calculation_error_test():
    vectors.v1 = [1]
    vectors.v2 = [1, 2]
    vectors.execution_flag = True
    with pytest.raises(ValueError):
        importlib.reload(vectors)
