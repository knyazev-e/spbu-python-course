import importlib
import math
import pytest

import project.task1.vectors as vectors


def test_scalar_multiplication():
    vectors.v1 = [1, 2, 3]
    vectors.v2 = [4, 5, 6]
    importlib.reload(vectors)
    assert vectors.scalar_multiplication_result == 32


def test_scalar_multiplication_error():
    vectors.v1 = [1, 2]
    vectors.v2 = [1]
    with pytest.raises(ValueError):
        importlib.reload(vectors)

    vectors.v1 = [1]
    vectors.v2 = [1]


def test_vector_sum():
    vectors.v1 = [1, 2, 3]
    vectors.v2 = [4, 5, 6]
    importlib.reload(vectors)
    assert vectors.vector_sum_result == [5, 7, 9]


def test_vector_sum_error():
    vectors.v1 = [1, 2]
    vectors.v2 = [1]
    with pytest.raises(ValueError):
        importlib.reload(vectors)

    vectors.v1 = [1]
    vectors.v2 = [1]


def test_length():
    vectors.v = [3, 4]
    importlib.reload(vectors)
    assert math.isclose(vectors.vector_length, 5.0)
    vectors.v = []
    importlib.reload(vectors)
    assert vectors.vector_length == 0.0


def test_angle_calculation():
    vectors.v1 = [1, 0]
    vectors.v2 = [0, 1]
    importlib.reload(vectors)
    assert math.isclose(vectors.angle, math.pi / 2)


def test_angle_calculation_error():
    vectors.v1 = [1]
    vectors.v2 = [1, 2]
    with pytest.raises(ValueError):
        importlib.reload(vectors)

    vectors.v1 = [1]
    vectors.v2 = [1]
