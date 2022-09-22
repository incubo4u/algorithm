from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        que = deque()
        normal_oranges = 0
        minutes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append((i, j))
                elif grid[i][j] == 1:
                    normal_oranges += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while que and normal_oranges:
            lenght = len(que)
            for _ in range(lenght):
                ny, nx = que.popleft()
                for _, (y, x) in enumerate(directions):
                    if not (0 <= ny + y < n and 0 <= nx + x < m):
                        continue
                    if grid[ny + y][nx + x] == 1:
                        grid[ny + y][nx + x] = 2
                        normal_oranges -= 1
                        que.append((ny + y, nx + x))
            minutes += 1
        if normal_oranges < 1:
            return minutes
        return -1
