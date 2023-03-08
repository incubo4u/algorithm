from ast import List
from math import ceil


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            t_req = sum(map(lambda b: ceil(b / mid), piles))
            if t_req <= h:
                r = mid
            else:
                l = mid + 1
        return l
