from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        flatten_mat = []
        for i in range(m):
            flatten_mat += mat[i]

        new_mat = []
        startIndex = 0
        for i in range(r):
            new_mat.append(flatten_mat[startIndex:startIndex + c])
            startIndex = startIndex + c

        return new_mat


print(Solution().matrixReshape([[1, 2, 3], [4, 5, 6], [7, 8, 9]], r=3, c=3))

# def matrixReshape(nums, r, c):
#     flat = sum(nums, [])
#     if len(flat) != r * c:
#         return nums
#     tuples = zip(*([iter(flat)] * c))
#     return map(list, tuples)
