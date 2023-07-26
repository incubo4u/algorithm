from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], h: float) -> int:
        n = len(dist)
        if n > ceil(h):
            return -1

        def check(kph):
            curr_h = 0
            for i, d in enumerate(dist):
                curr_h += ceil(d / kph) if i != n - 1 else d / kph
                if curr_h > h:
                    return
            return True

        l, r = 1, 10000000
        while l < r:
            kph = (l + r) // 2
            if not check(kph):
                l = kph + 1
            else:
                r = kph
        return int(l)
