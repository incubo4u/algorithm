from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] > 0:
            return -1
        seen = set()
        n = len(grid)
        que = deque()
        que.append([(0, 0)])
        directions = [(0, 1),(-1, 0),(0, -1),(1, 0),(-1, +1),(1, 1),(-1, -1),(1, -1)]
        while que:
            path = que.popleft()
            if path[-1] == (n - 1, n - 1):
                return len(path)
            ny, nx = path[-1]
            for _, (y, x) in enumerate(directions):
                if 0 <= ny + y < n and 0 <= nx + x < n:
                    if grid[ny + y][nx + x] < 1 and (ny + y, nx + x) not in seen:
                        seen.add((ny + y, nx + x))
                        que.append(path + [(ny + y, nx + x)])
        return -1