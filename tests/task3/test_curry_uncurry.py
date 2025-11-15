import pytest

from project.task3.curry_uncurry import curry_explicit, uncurry_explicit


def test_curry_basic_functionality():
    f3 = lambda x, y, z: f"<{x},{y},{z}>"
    curried = curry_explicit(f3, 3)
    assert curried(1)(2)(3) == "<1,2,3>"

    f2 = lambda x, y: x + y
    curried = curry_explicit(f2, 2)
    assert curried(5)(10) == 15

    f1 = lambda x: x * 2
    curried = curry_explicit(f1, 1)
    assert curried(5) == 10

    f0 = lambda: "returned_value"
    curried = curry_explicit(f0, 0)
    assert curried() == "returned_value"


def test_uncurry_basic_functionality():
    curried = lambda x: lambda y: lambda z: f"<{x},{y},{z}>"
    uncurried = uncurry_explicit(curried, 3)
    assert uncurried(1, 2, 3) == "<1,2,3>"

    curried = lambda x: lambda y: x + y
    uncurried = uncurry_explicit(curried, 2)
    assert uncurried(5, 10) == 15

    curried = lambda x: x * 2
    uncurried = uncurry_explicit(curried, 1)
    assert uncurried(5) == 10

    curried = lambda: "returned_value"
    uncurried = uncurry_explicit(curried, 0)
    assert uncurried() == "returned_value"


def test_curry_uncurry_roundtrip():
    original = lambda x, y, z: x * y + z
    curried = curry_explicit(original, 3)
    uncurried = uncurry_explicit(curried, 3)

    assert uncurried(2, 3, 4) == original(2, 3, 4)
    assert uncurried(5, 6, 7) == original(5, 6, 7)


def test_uncurry_curry_roundtrip():
    curried_func = lambda x: lambda y: lambda z: x * y * z
    uncurried = uncurry_explicit(curried_func, 3)
    re_curried = curry_explicit(uncurried, 3)

    assert re_curried(2)(3)(4) == curried_func(2)(3)(4)


def test_error_negative_arity():
    f = lambda x, y: x + y

    with pytest.raises(ValueError, match="non-negative"):
        curry_explicit(f, -1)

    with pytest.raises(ValueError, match="non-negative"):
        uncurry_explicit(f, -1)


def test_error_too_many_arguments_curry():
    f = lambda x, y: x + y
    curried = curry_explicit(f, 2)

    with pytest.raises(TypeError):
        curried(1)(2)(3)


def test_error_wrong_arity_uncurry():
    curried = lambda x: lambda y: x + y
    uncurried = uncurry_explicit(curried, 2)

    with pytest.raises(TypeError, match="Wrong number of arguments"):
        uncurried(1)

    with pytest.raises(TypeError, match="Wrong number of arguments"):
        uncurried(1, 2, 3)


def test_arity_freeze():
    curried_print = curry_explicit(print, 2)
    result = curried_print("hello")("world")

    assert result is None

    with pytest.raises(TypeError):
        curried_print("hello")("world")("extra")


def test_different_argument_types():
    f_str = lambda a, b: a + b
    curried_str = curry_explicit(f_str, 2)
    assert curried_str("hello")(" world") == "hello world"

    f_list = lambda a, b: a + b
    curried_list = curry_explicit(f_list, 2)
    assert curried_list([1, 2])([3, 4]) == [1, 2, 3, 4]

    f_mixed = lambda a, b: f"{type(a).__name__}:{a}, {type(b).__name__}:{b}"
    curried_mixed = curry_explicit(f_mixed, 2)
    result = curried_mixed(42)("text")
    assert "int:42" in result and "str:text" in result


@pytest.mark.parametrize("arity", [0, 1, 2, 3, 5])
def test_different_arities(arity):
    def test_func(*args):
        return sum(args) if args else 0

    curried = curry_explicit(test_func, arity)
    uncurried = uncurry_explicit(curried, arity)

    test_args = list(range(arity))
    expected = sum(test_args) if arity > 0 else 0

    if arity == 0:
        assert curried() == expected
        assert uncurried() == expected
    else:
        result_curried = curried
        for arg in test_args:
            result_curried = result_curried(arg)
        assert result_curried == expected

        assert uncurried(*test_args) == expected
