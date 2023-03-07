from typing import List


class Solution:

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, (min(time) * totalTrips)
        while l < r:
            mid = (l + r) // 2
            s = sum(map(lambda t: mid // t, time))
            if s >= totalTrips:
                r = mid
            else:
                l = mid + 1
        return l
