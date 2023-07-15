from bisect import bisect_right
from functools import cache


class Solution:

    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda e: e[0])
        n = len(events)
        INF = 10**9

        @cache
        def get_max(i, count, prev_end):
            if count > k:
                return -INF
            elif i > n - 1 or count == k:
                return 0
            j = bisect_right(events, prev_end, lo=i, key=lambda e: e[0])
            if j > n - 1:
                return 0

            start, end, val = events[j]
            return max(
                get_max(i + 1, count + 1, end) + val,
                get_max(i + 1, count, prev_end),
            )

        return get_max(0, 0, 0)
