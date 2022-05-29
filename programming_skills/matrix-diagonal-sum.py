from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    length = len(mat)
    sum_mat = 0
    for i in range(length):
        sum_mat += mat[i][i]
        sum_mat += mat[length - i - 1][i]

    if length % 2 == 1:
        mid = length // 2
        sum_mat -= mat[mid][mid]

    return sum_mat


print(diagonalSum(mat=[[1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1]]))
