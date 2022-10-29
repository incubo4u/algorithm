from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_r = len(mat)
        old_c = len(mat[0])
        if old_c * old_r != r * c:
            return mat
        new_mat = [[]]
        for i in range(old_r):
            for j in range(old_c):
                if len(new_mat[-1]) < c:
                    new_mat[-1].append(mat[i][j])
                else:
                    new_mat.append([mat[i][j]])
        return new_mat
