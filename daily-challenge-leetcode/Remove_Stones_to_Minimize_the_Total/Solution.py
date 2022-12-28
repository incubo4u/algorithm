from heapq import heapify, heappop, heappush
from typing import List


class Solution:

    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda p: -p, piles))
        heapify(piles)
        while k:
            p = heappop(piles)
            heappush(piles, p // 2)
            k -= 1
        return -sum(piles)