from functools import cache
from typing import List


class Solution:

    def minPathSum(self, G: List[List[int]]) -> int:
        n, m = len(G), len(G[0])

        @cache
        def traverse(i, j):
            if i > n - 1 or j > m - 1:
                return 20000
            if (i, j) == (n - 1, m - 1):
                return G[i][j]

            return min(traverse(i + 1, j), traverse(i, j + 1)) + G[i][j]

        return traverse(0, 0)
