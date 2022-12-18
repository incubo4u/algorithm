from functools import cache
from typing import List


class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = len(days)

        @cache
        def travel(i, valid):
            if i > d - 1:
                return 0
            if days[i] <= valid:
                return travel(i + 1, valid)
            return min(
                travel(i + 1, days[i]) + costs[0],
                travel(i + 1, days[i] + 6) + costs[1],
                travel(i + 1, days[i] + 29) + costs[2])

        return travel(0, 0)
