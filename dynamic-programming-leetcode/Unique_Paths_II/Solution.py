from functools import cache
from typing import List


class Solution:

    def uniquePathsWithObstacles(self, G: List[List[int]]) -> int:
        n, m = len(G), len(G[0])

        @cache
        def traverse(i, j):
            if i > n - 1 or j > m - 1 or G[i][j]:
                return 0
            if (i, j) == (n - 1, m - 1):
                return 1
            return traverse(i + 1, j) + traverse(i, j + 1)

        return traverse(0, 0)
