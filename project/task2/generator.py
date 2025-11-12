"""
Lazy stream data processing system.

This module provides:
- a generator function for lazy data production,
- a generic pipeline function for sequentially applying transformations,
- an aggregator function to materialize results into collections.
"""

from typing import Any, Callable, Generator, Iterable, List


def number_generator(start: int, finish: int) -> Generator[int, None, None]:
    """
    Lazily generates whole numbers in the specified range.

    Args:
        start (int): Starting number of the range (inclusive).
        finish (int): Ending number of the range (inclusive).

    Returns:
        Generator[int, None, None]: Generator yielding integers from start to finish.
    """

    for i in range(start, finish + 1):
        yield i


def apply_function(source: Iterable[Any], *operations: Callable[[Any], Any]) -> Any:
    """
    Applies a sequence of operations to the source data.

    Args:
        source (Iterable[Any]): Input iterable or generator.
        *operations (Callable[[Any], Any]): Functions each accepting one argument (iterable or value)
                                           and returning iterable or final value.

    Returns:
        Any: The final output after applying all operations.
    """

    result: Any = source
    for operation in operations:
        result = operation(result)
    return result


def wrap_result(result: Iterable[Any], collection_type: type = list) -> Iterable[Any]:
    """
    Aggregator function that converts a generator or iterable into a specified collection type.

    Args:
        result (Iterable[Any]): Input iterable or generator to be collected.
        collection_type (type): Type of collection to aggregate into (defaults to list).

    Returns:
        Iterable[Any]: Collection of the specified type containing all elements from the input.
    """

    return collection_type(result)
