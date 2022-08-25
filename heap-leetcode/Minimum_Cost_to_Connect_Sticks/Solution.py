import heapq
from typing import List


class Solution:
    def connectSticks(self, heap: List[int]) -> int:
        heapq.heapify(heap)
        cost = 0
        while len(heap) > 1:
            s = heapq.heappop(heap) + heapq.heappop(heap)
            heapq.heappush(heap, s)
            cost += s
        return cost
