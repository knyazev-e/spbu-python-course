from typing import Any, Callable
from copy import deepcopy
from inspect import signature, Parameter


class Evaluated:
    """Marker for evaluated default values."""

    def __init__(self, func: Callable[[], Any]):
        if not callable(func):
            raise TypeError("Evaluated requires a callable.")

        sig = signature(func)
        if len(sig.parameters) > 0:
            raise TypeError("Evaluated function must take no arguments.")

        self.func = func


class Isolated:
    """Marker for isolated (deep copied) arguments."""

    pass


def smart_args(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that handles Evaluated and Isolated default arguments values.

    For Evaluated: calls the function to get a default value at the call time.
    For Isolated: makes a deep copy of the passed argument.
    Only supports keyword arguments.
    """

    sig = signature(func)

    for param_name, param in sig.parameters.items():
        if param.default is not param.empty:
            if isinstance(param.default, Evaluated) and isinstance(
                param.default, Isolated
            ):
                raise ValueError(
                    f"Parameter '{param_name}' cannot use both Evaluated and Isolated at the same time."
                )

    def wrapper(*args, **kwargs) -> Any:
        bound = sig.bind(*args, **kwargs)
        provided_args = set(bound.arguments.keys())
        bound.apply_defaults()
        final_args = bound.arguments.copy()

        for param_name, param in sig.parameters.items():
            if param.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD):
                continue

            if isinstance(param.default, Evaluated) and param_name not in provided_args:
                final_args[param_name] = param.default.func()
            elif (
                isinstance(param.default, Isolated) and param_name not in provided_args
            ):
                raise TypeError(f"Isolated argument '{param_name}' must be provided.")
            elif isinstance(param.default, Isolated) and param_name in provided_args:
                final_args[param_name] = deepcopy(final_args[param_name])

        positional_args = []
        keyword_args = {}

        for param_name, param in sig.parameters.items():
            if param_name in final_args:
                if param.kind == Parameter.POSITIONAL_ONLY:
                    positional_args.append(final_args[param_name])
                else:
                    keyword_args[param_name] = final_args[param_name]

        return func(*positional_args, **keyword_args)

    return wrapper
