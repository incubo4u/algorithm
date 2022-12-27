from typing import List


class Solution:

    def maximumBags(self, capacity: List[int], rocks: List[int],
                    additionalRocks: int) -> int:
        ans = 0
        fun = lambda t: t[0] - t[1]
        for _, (c, r) in enumerate(sorted(zip(capacity, rocks), key=fun)):
            additionalRocks -= c - r
            if additionalRocks >= 0:
                ans += 1
            else:
                break
        return ans
