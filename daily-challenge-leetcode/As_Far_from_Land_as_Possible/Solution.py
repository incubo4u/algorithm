from collections import deque
from itertools import product
from typing import List


class Solution:

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        water = False
        que = deque()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        seen = [[None] * n for _ in range(n)]

        def mark(x, y, d):
            seen[x][y] = d
            que.append((x, y))

        for _, (x, y) in enumerate(product(range(n), range(n))):
            if grid[x][y]:
                mark(x, y, 0)
            else:
                water = True

        if not que or not water:
            return -1

        while que:
            x, y = que.popleft()
            for dx, dy in directions:
                if n > x+dx >= 0 and \
                   n > y+dy >= 0 and \
                   seen[x+dx][y+dy] is None :

                    mark(x + dx, y + dy, seen[x][y] + 1)

        return max(map(max, seen))
