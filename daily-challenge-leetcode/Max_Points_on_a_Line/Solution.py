from collections import defaultdict
from typing import List


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        d = defaultdict(int)
        INF = 10**4 + 1 
        for x, y in points:
            for x1, y1 in points:
                if (x1, y1) == (x, y):
                    continue
                slope = (y1 - y) / (x1 - x) if (x) != (x1) else INF
                key = (x, y, slope)
                d[key] += 1
                ans = max(ans, d[key])
        return ans + 1
