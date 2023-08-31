from ast import List
from functools import cache


class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges = [(i - r, i + r) for i, r in enumerate(ranges) if r]
        ranges.sort()
        N = len(ranges)
        INF = 10**5

        @cache
        def get_min(i, last_r):
            if i > N - 1:
                return 0 if last_r >= n else INF
            l, r = ranges[i]
            if l - last_r >= 1:
                return INF
            return min(get_min(i + 1, r) + 1, get_min(i + 1, last_r))

        return ans if (ans := get_min(0, 0)) != INF else -1
