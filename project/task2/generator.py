"""
Lazy stream data processing system.

This module provides:
- a generator function for lazy data production,
- a generic pipeline function for sequentially applying transformations,
- an aggregator function to materialize results into collections.
"""

from typing import Any, Callable, Generator, Iterable, List


def input_data_generator(input_collection: Iterable[Any]) -> Generator[Any, None, None]:
    """
    Lazily yields elements from any inputted iterable collection.

    Args:
        input_collection (Iterable[Any]): Input collection to yield elements from.

    Returns:
        Generator[Any, None, None]: Generator yielding the elements.
    """

    for i in input_collection:
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


def wrap_result(result: Iterable[Any]) -> List[Any]:
    """
    Aggregator function that converts a generator or iterable into a list.

    Args:
        data (Iterable[Any]): Input iterable or generator.

    Returns:
        List[Any]: List containing all elements from the input.
    """

    return list(result)
