from itertools import product


class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        MOD = (10**9) + 7
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        memo = [[0] * N for _ in range(M)]

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]

            curr = 1
            for x, y in directions:
                if (xj := x + j) < 0 or xj > N - 1 or (yi := y + i) < 0 or yi > M - 1:
                    continue
                if grid[yi][xj] < grid[i][j]:
                    curr += dfs(yi, xj)
            memo[i][j] = curr
            return memo[i][j]

        ans = 0
        for _, (i, j) in enumerate(product(range(M), range(N))):
            ans += dfs(i, j)
        return ans % MOD
