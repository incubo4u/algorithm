from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        hq = [(0, (0, 0))]
        n, m = len(heights), len(heights[0])
        seen = set((0, 0))
        max_w = 0
        while hq:
            w, (y, x) = heappop(hq)
            max_w = max(max_w, w)
            seen.add((y, x))
            if y == n - 1 and x == m - 1:
                return max_w
            for i, j in directions:
                next_y, next_x = y + i, x + j
                if 0 <= next_y < n and 0 <= next_x < m and (next_y, next_x) not in seen:
                    w = abs(heights[y][x] - heights[next_y][next_x])
                    heappush(hq, (w, (next_y, next_x)))
