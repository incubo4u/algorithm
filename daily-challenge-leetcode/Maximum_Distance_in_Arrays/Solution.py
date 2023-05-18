from heapq import heappop, heappush
from typing import List


class Solution:
    #todo remove the hq
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small, big = [], []
        for i, arr in enumerate(arrays):
            heappush(small, (arr[0], i))
            heappush(big, (-arr[-1], i))
        if small[0][1] == big[0][1]:
            s, _ = heappop(small)
            b, _ = heappop(big)
            return max(-b - small[0][0], -big[0][0] - s)
        return -big[0][0] - small[0][0]
