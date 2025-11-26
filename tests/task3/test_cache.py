import pytest

from project.task3.cache import cache
from project.task3.curry_uncurry import curry_explicit, uncurry_explicit


def test_cache_basic():
    calls = 0

    @cache(3)
    def func(x, y=0):
        nonlocal calls
        calls += 1
        return x + y

    assert func(1, 2) == 3
    assert calls == 1
    assert func(1, 2) == 3
    assert calls == 1

    assert func(1, y=2) == 3
    assert calls == 2


def test_cache_deletion_and_disabled_caching():
    calls = 0

    @cache(2)
    def func(x):
        nonlocal calls
        calls += 1
        return x

    func(1)
    func(2)
    assert calls == 2
    func(3)
    func(1)
    assert calls == 4

    @cache(0)
    def no_cache(x):
        nonlocal calls
        calls += 1
        return x

    no_cache(1)
    no_cache(1)
    assert calls == 6


def test_cache_with_curry():
    calls = 0

    def func(x, y):
        nonlocal calls
        calls += 1
        return x * y

    cached = cache(2)(func)
    curried = curry_explicit(cached, 2)

    curried(3)(4)
    assert calls == 1
    curried(3)(4)
    assert calls == 1


def test_cache_error():
    with pytest.raises(ValueError):

        @cache(-1)
        def func():
            pass
