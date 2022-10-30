from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = ((-1, 0),  (0, 1),(1, 0), (0, -1))
        m, n = len(grid), len(grid[0])
        que = deque()
        que.append((0, 0, 0, k))
        seen = set()
        
        if k >= m + n - 2:
            return m + n - 2

        while que:
            pos = que.popleft()

            if pos[0] == m - 1 and pos[1] == n - 1:
                return pos[2]
            

            if (pos[0], pos[1], pos[3]) in seen:
                continue
            seen.add((pos[0], pos[1], pos[3]))

            for _, (y, x) in enumerate(directions):
                new_pos = (pos[0] + y, pos[1] + x, pos[2] + 1, pos[3])

                if m > new_pos[0] >= 0 and n > new_pos[1] >= 0:

                    if pos[3] > 0 and grid[new_pos[0]][new_pos[1]] == 1:
                        que.append((new_pos[0], new_pos[1], new_pos[2], pos[3] - 1))

                    elif grid[new_pos[0]][new_pos[1]] == 0:
                        que.append(new_pos)

        return -1
