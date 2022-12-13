from functools import cache
from typing import List


class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        @cache
        def find(i, j):
            if i > n - 1:
                return 0
            best = 10000
            for r, c in ((i + 1, j - 1), (i + 1, j), (i + 1, j + 1)):
                if c > m - 1 or 0 > c:
                    continue
                best = min(find(r, c) + matrix[i][j], best)
            return best

        ans = 10000
        for j in range(m):
            ans = min(ans, find(0, j))
        return ans
