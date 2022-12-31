from itertools import product


class Solution:

    def uniquePathsIII(self, grid) -> int:
        ans = zeros = 0
        m, n = len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 0:
                zeros += 1
            elif grid[i][j] == 1:
                start = (i, j)
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def dfs(i, j, zeros):
            grid[i][j] = 3

            for di, dj in directions:
                pi, pj = i + di, j + dj
                if 0 <= pi < m and 0 <= pj < n:
                    if grid[pi][pj] == 0:
                        dfs(pi, pj, zeros - 1)
                    if grid[pi][pj] == 2 and zeros == 0:
                        nonlocal ans
                        ans += 1

            grid[i][j] = 0
            return

        dfs(*start, zeros)# type: ignore        return ans
 