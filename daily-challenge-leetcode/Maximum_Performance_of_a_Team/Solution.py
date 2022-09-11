from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        workers = list(zip(efficiency, speed))
        workers.sort(reverse=True)
        minheap = []
        best, maxSpeed = 0, 0
        for _, (e, s) in enumerate(workers):
            if len(minheap) > k - 1:
                maxSpeed -= heappop(minheap)
            heappush(minheap, s)
            maxSpeed += s
            best = max(best, e * maxSpeed)
        return best % 1000000007
