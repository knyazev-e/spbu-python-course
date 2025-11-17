import pytest

from project.task3.smart_args import smart_args, Evaluated, Isolated
from copy import deepcopy


def test_isolated():
    original = {"a": 1}

    @smart_args
    def modify(*, num=10, data=Isolated()):
        data["b"] = 2
        return num, data

    result_num, result_data = modify(data=original, num=5)
    assert result_num == 5
    assert result_data == {"a": 1, "b": 2}
    assert original == {"a": 1}

    result_num, result_data = modify(data=original)
    assert result_num == 10


def test_evaluated():
    counter = 0

    def count():
        nonlocal counter
        counter += 1
        return counter

    @smart_args
    def get_values(*, static_val=100, dynamic_val=Evaluated(count)):
        return static_val, dynamic_val

    assert get_values() == (100, 1)
    assert get_values() == (100, 2)

    assert get_values(static_val=50, dynamic_val=99) == (50, 99)


def test_isolated_required():
    @smart_args
    def func(*, normal=5, required=Isolated()):
        return normal, required

    with pytest.raises(TypeError):
        func()


def test_evaluated_errors():
    def invalid_func(x):
        return x

    with pytest.raises(TypeError):
        Evaluated("not callable")

    with pytest.raises(TypeError):
        Evaluated(invalid_func)
