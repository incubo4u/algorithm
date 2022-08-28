from heapq import heappop, heappush
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        diagonals = h + w - 1

        def getDiagonal(i, j):
            diagonal = []
            while i != h and j != w:
                heappush(diagonal, mat[i][j])
                i += 1
                j += 1
            return diagonal

        def replaceDiagonal(newOne, i, j):
            while i != h and j != w:
                mat[i][j] = heappop(newOne)
                i += 1
                j += 1

        for j in range(w):
            replaceDiagonal(getDiagonal(0, j), 0, j)
        for i in range(1, h):
            replaceDiagonal(getDiagonal(i, 0), i, 0)
        return mat
