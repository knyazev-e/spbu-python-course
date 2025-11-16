from typing import Any, Callable
from collections import OrderedDict


def cache(cache_size: int = 0) -> Callable:
    """
    Caching decorator that stores the function execution results.

    Args:
        cache_size: number of recent results to cache (0 = no caching)

    Returns:
        the decorated function with caching
    """
    if cache_size < 0:
        raise ValueError("Cache size must be non-negative")

    def decorator(func: Callable) -> Callable:
        cache_dict: OrderedDict = OrderedDict()

        def wrapper(*args, **kwargs) -> Any:
            if cache_size == 0:
                return func(*args, **kwargs)

            key = (args, tuple(sorted(kwargs.items())))

            if key in cache_dict:
                result = cache_dict.pop(key)
                cache_dict[key] = result
                return result

            result = func(*args, **kwargs)

            cache_dict[key] = result

            if len(cache_dict) > cache_size:
                cache_dict.popitem(last=False)

            return result

        return wrapper

    return decorator
