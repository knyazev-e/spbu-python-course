from typing import Any, Callable


def curry_explicit(function: Callable[..., Any], arity: int) -> Callable[..., Any]:
    """
    Converts a function of multiple arguments into a sequence of one-argument functions.

    Args:
        function: the function to curry
        arity: number of arguments the function expects

    Returns:
        curried version of the function
    """

    if arity < 0:
        raise ValueError("The arity must be a non-negative number.")

    def curried(*args):
        if len(args) > arity:
            raise TypeError(f"Too many arguments passed. Expected {arity} arguments.")
        elif len(args) == arity:
            return function(*args)
        elif len(args) < arity:
            return lambda next_arg: curried(*args, next_arg)

    return curried


def uncurry_explicit(function: Callable[..., Any], arity: int) -> Callable[..., Any]:
    """
    Converts a curried function back into a multi-argument function.

    Args:
        function: the curried function
        arity: number of arguments the original function expected

    Returns:
        uncurried version of the function
    """

    if arity < 0:
        raise ValueError("The arity must be a non-negative number.")

    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Wrong number of arguments. Expected {arity} arguments.")

        result = function
        for arg in args:
            result = result(arg)

        return result() if arity == 0 else result

    return uncurried
