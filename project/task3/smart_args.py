from typing import Any, Callable
from copy import deepcopy
from inspect import signature


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
            if param.kind != param.KEYWORD_ONLY:
                raise ValueError(
                    f"smart_args only supports keyword-only arguments. Parameter '{param_name}' is not keyword-only"
                )

    def wrapper(**kwargs) -> Any:
        bound = sig.bind_partial()
        bound.apply_defaults()
        default_values = bound.arguments

        final_kwargs = default_values.copy()
        final_kwargs.update(kwargs)

        for param_name, param in sig.parameters.items():
            if isinstance(param.default, Evaluated) and param_name not in kwargs:
                final_kwargs[param_name] = param.default.func()
            elif isinstance(param.default, Isolated) and param_name not in kwargs:
                raise TypeError(f"Isolated argument '{param_name}' must be provided.")
            elif isinstance(param.default, Isolated) and param_name in kwargs:
                final_kwargs[param_name] = deepcopy(kwargs[param_name])

        return func(**final_kwargs)

    return wrapper
