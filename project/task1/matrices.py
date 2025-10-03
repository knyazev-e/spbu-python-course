from typing import List


def transpose(m: List[List[float]]) -> List[List[float]]:
    """
    Returns the transpose of the given matrix.

    Parameters:
        m (List[List[float]]): The input matrix to transpose.

    Returns:
        List[List[float]]: The transposed matrix.

    Raises:
        ValueError: If the matrix is empty or rows have inconsistent lengths.
    """
    if not m or all(len(row) == 0 for row in m):
        raise ValueError("The matrix is empty.")
    elif any(len(m[0]) != len(row) for row in m):
        raise ValueError(
            "A matrix must have a constant number of elements in each row."
        )
    else:
        return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


def matrix_sum(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    """
    Computes the element-wise sum of two matrices of the same size.

    Parameters:
        m1 (List[List[float]]): First matrix.
        m2 (List[List[float]]): Second matrix.

    Returns:
        List[List[float]]: Resulting matrix after addition.

    Raises:
        ValueError: If matrices are empty, of different sizes, or have inconsistent row lengths.
    """
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
        return [
            [m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))
        ]


def matrix_multiplication(
    m1: List[List[float]], m2: List[List[float]]
) -> List[List[float]]:
    """
    Performs matrix multiplication of two compatible matrices.

    Parameters:
        m1 (List[List[float]]): First matrix.
        m2 (List[List[float]]): Second matrix.

    Returns:
        List[List[float]]: The product matrix.

    Raises:
        ValueError: If matrices are empty, have inconsistent row lengths, or dimensions are incompatible for multiplication.
    """
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
        return [
            [
                sum(m1[i][j] * m2[j][k] for j in range(len(m1[0])))
                for k in range(len(m2[0]))
            ]
            for i in range(len(m1))
        ]
