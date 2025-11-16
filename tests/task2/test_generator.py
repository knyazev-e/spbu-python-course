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
        ([lambda x: x + 1], [2, 3, 4]),
        ([lambda x: x if x % 2 == 0 else None], [2]),
        ([lambda x: x * 2, lambda x: x if x > 3 else None], [4, 6]),
    ],
)
def test_apply_function(operations, expected):
    data = [1, 2, 3]
    result = apply_function(data, *operations)
    filtered_result = [x for x in result if x is not None]
    assert filtered_result == expected


def test_custom_functions_double():
    data = [1, 2, 3]
    result = apply_function(data, double)
    assert list(result) == [2, 4, 6]


def test_custom_functions_is_even():
    data = [1, 2, 3]
    result = apply_function(data, lambda x: x if is_even(x) else None)
    filtered_result = [x for x in result if x is not None]
    assert filtered_result == [2]


def test_custom_functions_is_even_map():
    data = [1, 2, 3]
    result = apply_function(data, is_even)
    assert list(result) == [False, True, False]


def test_multiple_custom_functions():
    data = [1, 2, 3]
    result = apply_function(data, double, compound_expression)
    assert list(result) == [24, 28, 32]


def test_laziness_verification():
    execution_trace = []

    def traced_double_function(x):
        execution_trace.append(f"processed_{x}")
        return x * 2

    generator = number_generator(1, 5)
    processed = apply_function(generator, traced_double_function)

    assert execution_trace == []

    first_item = next(processed)
    assert first_item == 2
    assert execution_trace == ["processed_1"]

    second_item = next(processed)
    assert second_item == 4
    assert execution_trace == ["processed_1", "processed_2"]
