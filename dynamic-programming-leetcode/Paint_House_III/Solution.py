from functools import cache
from typing import List


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], n: int, k: int,
                target: int) -> int:
        INF = 10000000

        @cache
        def paint(i, lc, grp):

            if i > n - 1:
                return 0 if grp == target else INF

            if grp > target:
                return INF

            if houses[i]:
                if houses[i] - 1 != lc:
                    return paint(i + 1, houses[i] - 1, grp + 1)
                else:
                    return paint(i + 1, houses[i] - 1, grp)

            return min(
                map(
                    lambda c: paint(i + 1, c, grp) + cost[i][c]
                    if c == lc else paint(i + 1, c, grp + 1) + cost[i][c],
                    range(k)))

        return ans if (ans := paint(0, -1, 0)) < INF else -1
