from typing import List


class Solution:

    def findMinArrowShots(self, P: List[List[int]]) -> int:
        P.sort(key=lambda p: p[1])
        ans = 1
        last_end = P[0][1]
        for start, end in P[1:]:
            if start > last_end:
                ans += 1
                last_end = end
        return ans
