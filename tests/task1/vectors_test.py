import pytest
import math

from project.task1.vectors import scalar_multiplication, vector_sum, length, eval_angle


def scalar_multiplication_test():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    assert scalar_multiplication(v1, v2) == 32


def scalar_multiplication_error_test():
    with pytest.raises(ValueError):
        scalar_multiplication([1, 2], [1])


def vector_sum_test():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    assert vector_sum(v1, v2) == [5, 7, 9]


def vector_sum_error_test():
    with pytest.raises(ValueError):
        vector_sum([1, 2], [1])


def length_test():
    assert math.isclose(length([3, 4]), 5.0)
    assert length([]) == 0.0


def angle_calculation_test():
    v1 = [1, 0]
    v2 = [0, 1]
    assert math.isclose(eval_angle(v1, v2), math.pi / 2)


def angle_calculation_error_test():
    with pytest.raises(ValueError):
        eval_angle([1], [1, 2])
