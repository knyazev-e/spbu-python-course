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


v: List[float] = []
v1: List[float] = []
v2: List[float] = []
execution_flag = False

if execution_flag:
    if len(v1) == len(v2):
        scalar_multiplication_result: float = sum(v1[i] * v2[i] for i in range(len(v1)))
    else:
        raise ValueError("The vectors must be the same length to be multiplied.")

    if len(v1) == len(v2):
        vector_sum_result: List[float] = [v1[i] + v2[i] for i in range(len(v1))]
    else:
        raise ValueError("The vectors must be the same length to perform addition.")

    if len(v) == 0:
        vector_length: float = 0.0
    else:
        vector_length: float = math.sqrt(sum(v[i] ** 2 for i in range(len(v))))

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
