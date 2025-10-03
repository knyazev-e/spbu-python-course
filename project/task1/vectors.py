"""
Vector operations module.

Contains input vectors and computes:
- scalar_multiplication_result
- vector_sum_result
- length
- angle

All computations run on module import or reload.

Raises ValueError on invalid inputs.
"""

import math
from typing import List


v = []
v1 = []
v2 = []
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
        length: float = 0.0
    else:
        length: float = math.sqrt(
            sum(v_length_vec[i] ** 2 for i in range(len(v_length_vec)))
        )

    if len(v1) == len(v2):
        try:
            dot_product = sum(v1[i] * v2[i] for i in range(len(v1)))
            len_v1 = math.sqrt(sum(v1[i] ** 2 for i in range(len(v1))))
            len_v2 = math.sqrt(sum(v2[i] ** 2 for i in range(len(v2))))
            angle: float = math.acos(dot_prod / (len_v1 * len_v2))
        except ZeroDivisionError:
            angle = float("nan")
    else:
        raise ValueError(
            "The vectors must be the same length to calculate the angle between them."
        )
