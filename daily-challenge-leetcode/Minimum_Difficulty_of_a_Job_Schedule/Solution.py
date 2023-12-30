from functools import cache
from math import inf


class Solution:

    def minDifficulty(self, cost: list[int], d: int) -> int:
        ans = inf
        n = len(cost)

        @cache
        def do(i, day_cost, day):
            if day < 0:
                return inf

            if i > n - 1:
                return day_cost if not day else inf

            job_c = cost[i]

            return min(
                do(i + 1, max(day_cost, job_c), day),
                do(i + 1, job_c, day - 1) + day_cost,
            )

        ans = do(0, 0, d)
        if ans != inf:
            return ans
        return -1
