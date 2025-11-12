import pytest
from project.task2.generator import number_generator, apply_function, wrap_result


def double(x):
    return x * 2


def is_even(x):
    return x % 2 == 0


def compound_expression(x):
    return (x + 10) * 2


def test_number_generator():
    gen = number_generator(1, 3)
    assert list(gen) == [1, 2, 3]


def test_wrap_result():
    data = (x for x in range(5))
    collected = wrap_result(data)
    assert collected == [0, 1, 2, 3, 4]


def test_wrap_result_parameterized():
    data = (x for x in range(3))
    assert wrap_result(data, tuple) == (0, 1, 2)


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


def test_custom_functions_double():
    data = [1, 2, 3]
    result = apply_function(data, double)
    assert list(result) == [2, 4, 6]


def test_custom_functions_is_even():
    data = [1, 2, 3]
    result = apply_function(data, lambda y: map(is_even, y))
    assert list(result) == [False, True, False]


def test_multiple_custom_functions():
    data = [1, 2, 3, 4, 5]
    result = apply_function(
        data, lambda d: filter(is_even, d), double, compound_expression
    )
    assert list(result) == [28, 36]


def test_laziness_verification():
    execution_trace = []

    def traced_double_function(x):
        execution_trace.append(f"processed_{x}")
        return x * 2

    generator = number_generator(1, 5)
    processed = apply_function(generator, lambda d: map(traced_double_function, d))

    assert execution_trace == []

    first_item = next(processed)
    assert first_item == 2
    assert execution_trace == ["processed_1"]

    second_item = next(processed)
    assert second_item == 4
    assert execution_trace == ["processed_1", "processed_2"]
