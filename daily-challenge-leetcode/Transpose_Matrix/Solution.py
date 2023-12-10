from itertools import product


class Solution:

    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n, m = len(matrix), len(matrix[0])
        t = [[0] * n for i in range(m)]
        for _, (i, j) in enumerate(product(range(n), range(m))):
            t[j][i] = matrix[i][j]
        return t
