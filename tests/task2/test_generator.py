import pytest
from project.task2.generator import input_data_generator, apply_function, wrap_result


def test_input_data_generator():
    data = [1, 2, 3]
    gen = input_data_generator(data)
    assert list(gen) == data


@pytest.mark.parametrize(
    "operations, expected",
    [
        ([lambda d: map(lambda x: x + 1, d)], [2, 3, 4]),
        ([lambda d: filter(lambda x: x % 2 == 0, d)], [2]),
        (
            [lambda d: map(lambda x: x * 2, d), lambda d: filter(lambda x: x > 3, d)],
            [4, 6],
        ),
    ],
)
def test_apply_function(operations, expected):
    data = [1, 2, 3]
    result = apply_function(data, *operations)
    assert list(result) == expected


def test_wrap_result():
    data = (x for x in range(5))
    collected = wrap_result(data)
    assert collected == [0, 1, 2, 3, 4]
