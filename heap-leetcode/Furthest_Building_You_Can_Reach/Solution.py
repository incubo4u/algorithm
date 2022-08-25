import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap = []
        lenght = len(heights)
        for i in range(1, lenght):
            if heights[i - 1] >= heights[i]:
                continue
            missing = heights[i] - heights[i - 1]
            if bricks - missing >= 0:
                bricks -= missing
                heapq.heappush(maxheap, -missing)
            elif ladders > 0:
                if (
                    maxheap
                    and bricks + (-maxheap[0]) >= missing
                    and (-maxheap[0]) >= missing
                ):
                    ladders -= 1
                    bricks = -maxheap[0] + bricks - missing
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, -missing)
                else:
                    ladders -= 1
            else:
                return i - 1 if i - 1 >= 0 else 0
        return lenght - 1
