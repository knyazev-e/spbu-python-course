"""
Vector operations module.

Contains input vectors and computes:
- scalar_multiplication_result
- vector_sum_result
- vector_length
- angle

All computations run on module import or reload.

Raises ValueError on invalid inputs.
"""

import math
from typing import List

if "v" not in globals():
    v: List[float] = [1]
if "v1" not in globals():
    v1: List[float] = [1]
if "v2" not in globals():
    v2: List[float] = [1]


if len(v1) == len(v2):
    scalar_multiplication_result: float = sum(v1[i] * v2[i] for i in range(len(v1)))
else:
    raise ValueError("The vectors must be the same length to be multiplied.")

if len(v1) == len(v2):
    vector_sum_result: List[float] = [v1[i] + v2[i] for i in range(len(v1))]
else:
    raise ValueError("The vectors must be the same length to perform addition.")

vector_length: float = 0.0

if len(v) == 0:
    vector_length = 0.0
else:
    vector_length = math.sqrt(sum(v[i] ** 2 for i in range(len(v))))

if len(v1) == len(v2):
    try:
        dot_product = sum(v1[i] * v2[i] for i in range(len(v1)))
        len_v1 = math.sqrt(sum(v1[i] ** 2 for i in range(len(v1))))
        len_v2 = math.sqrt(sum(v2[i] ** 2 for i in range(len(v2))))
        angle: float = math.acos(dot_product / (len_v1 * len_v2))
    except ZeroDivisionError:
        angle = float("nan")
else:
    raise ValueError(
        "The vectors must be the same length to calculate the angle between them."
    )
