import math
from typing import List


def scalar_multiplication(v1: List[float], v2: List[float]) -> float:
    """
    Calculates the scalar (dot) product of two vectors.

    Parameters:
        v1 (List[float]): First vector.
        v2 (List[float]): Second vector.

    Returns:
        float: The scalar product.

    Raises:
        ValueError: If the vectors have different lengths.
    """
    if len(v1) == len(v2):
        return sum(v1[i] * v2[i] for i in range(len(v1)))
    else:
        raise ValueError("The vectors must be the same length to be multiplied.")


def vector_sum(v1: List[float], v2: List[float]) -> List[float]:
    """
    Computes the sum of two vectors.

    Parameters:
        v1 (List[float]): First vector.
        v2 (List[float]): Second vector.

    Returns:
        List[float]: The resulting vector after addition.

    Raises:
        ValueError: If the vectors have different lengths.
    """
    if len(v1) == len(v2):
        return [v1[i] + v2[i] for i in range(len(v1))]
    else:
        raise ValueError("The vectors must be the same length to perform addition.")


def length(v: List[float]) -> float:
    """
    Calculates the length of a vector.

    Parameters:
        v (List[float]): The input vector.

    Returns:
        float: The length of the vector.
    """
    if len(v) == 0:
        return 0.0
    else:
        return (sum(v[i] ** 2 for i in range(len(v)))) ** 0.5


def eval_angle(v1: List[float], v2: List[float]) -> float:
    """
    Calculates the angle in radians between two vectors.

    Parameters:
        v1 (List[float]): First vector.
        v2 (List[float]): Second vector.

    Returns:
        float: The angle in radians between the vectors.

    Raises:
        ValueError: If the vectors have different lengths.
    """
    if len(v1) == len(v2):
        return math.acos(scalar_multiplication(v1, v2) / (length(v1) * length(v2)))
    else:
        raise ValueError(
            "The vectors must be the same length to calculate the angle between them."
        )
