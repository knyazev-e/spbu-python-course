"""
Matrix operations module.

Contains input matrices and computes:
- transposition_result
- matrix_sum_result
- matrix_multiplication_result

All computations run on module import or reload.

Raises ValueError on invalid inputs.
"""

from typing import List

m = [[]]
m1 = [[]]
m2 = [[]]
execution_flag = False

if execution_flag:
    if not m or all(len(row) == 0 for row in m):
        raise ValueError("The matrix is empty.")
    elif any(len(m[0]) != len(row) for row in m):
        raise ValueError(
            "A matrix must have a constant number of elements in each row."
        )
    else:
        transposition_result: List[List[float]] = [
            [m[i][j] for i in range(len(m))] for j in range(len(m[0]))
        ]

    if (
        len(m1) == 0
        or len(m2) == 0
        or all(len(row) == 0 for row in m1)
        or all(len(row) == 0 for row in m2)
    ):
        raise ValueError("The matrices must be non-empty.")
    elif any(len(m1[0]) != len(row) for row in m1) or any(
        len(m2[0]) != len(row) for row in m2
    ):
        raise ValueError(
            "A matrix must have a constant number of elements in each row."
        )
    elif len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("The matrices must be the same size.")
    else:
        matrix_sum_result: List[List[float]] = [
            [m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))
        ]

    if (
        len(m1) == 0
        or len(m2) == 0
        or all(len(row) == 0 for row in m1)
        or all(len(row) == 0 for row in m2)
    ):
        raise ValueError("The matrices must be non-empty.")
    elif any(len(m1[0]) != len(row) for row in m1) or any(
        len(m2[0]) != len(row) for row in m2
    ):
        raise ValueError(
            "A matrix must have a constant number of elements in each row."
        )
    elif len(m1[0]) != len(m2):
        raise ValueError(
            "The number of columns in the first matrix must equal the number of rows in the second matrix."
        )
    else:
        matrix_multiplication_result: List[List[float]] = [
            [
                sum(m1[i][j] * m2[j][k] for j in range(len(m1[0])))
                for k in range(len(m2[0]))
            ]
            for i in range(len(m1))
        ]
