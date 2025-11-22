import pytest

from project.task3.smart_args import smart_args, Evaluated, Isolated
from copy import deepcopy


def test_isolated():
    original_dict = {"a": 1}

    @smart_args
    def modify(pos_only, /, pos_or_kw=10, *, kw_only=Isolated()):
        kw_only["modified"] = pos_only + pos_or_kw
        return kw_only

    result = modify(5, 3, kw_only=original_dict)
    assert result == {"a": 1, "modified": 8}
    assert original_dict == {"a": 1}


def test_evaluated():
    counter = 0

    def count():
        nonlocal counter
        counter += 1
        return counter

    @smart_args
    def get_values(pos_only, /, pos_or_kw=50, *, dynamic_val=Evaluated(count)):
        return pos_only, pos_or_kw, dynamic_val

    assert get_values(10) == (10, 50, 1)
    assert get_values(20) == (20, 50, 2)

    assert get_values(30, 40, dynamic_val=99) == (30, 40, 99)


def test_isolated_required():
    @smart_args
    def function(arg1=Isolated(), /, arg2=Isolated(), *, arg3=Isolated()):
        return arg1, arg2, arg3

    with pytest.raises(TypeError):
        function(arg2=3, arg3=0)

    with pytest.raises(TypeError):
        function(1, 2)

    with pytest.raises(TypeError):
        function(1, arg3=20)

    assert function(1, 2, arg3=3) == (1, 2, 3)


def test_evaluated_errors():
    def invalid_func(x):
        return x

    with pytest.raises(TypeError):
        Evaluated("not callable")

    with pytest.raises(TypeError):
        Evaluated(invalid_func)
