from functools import cache


class Solution:

    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts.sort()
        INF = 10000000

        @cache
        def cut(left, right, start, end):
            if start >= end:
                return 0
            best = INF
            for i in range(start, end):
                c = cuts[i]
                best = min(
                    best,
                    cut(left, c, start, i) + cut(c, right, i + 1, end) +
                    right - left,
                )
            return best

        return cut(0, n, 0, len(cuts))
