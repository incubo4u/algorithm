import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) != 1:
            heapq.heappush(stones, -abs(heapq.heappop(stones) - heapq.heappop(stones)))
        return -stones[0]
