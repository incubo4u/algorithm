from typing import Deque, List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
        n, m = len(maze), len(maze[0])
        y, x = entrance
        que = Deque([(y, x, 0)])
        while que:

            y, x, c = que.popleft()

            if y > n - 1 or x > m - 1 or y < 0 or x < 0 or maze[y][x] == "+":
                continue

            if y == n - 1 or y == 0 or x == m - 1 or x == 0:
                if (y, x) != (entrance[0], entrance[1]):
                    return c
                    
            maze[y][x] = "+"

            for dy, dx in directions:
                que.append((dy + y, dx + x, c + 1))

        return -1
