class Solution:

    def maximalSquare(self, mat) -> int:
        n, m = len(mat), len(mat[0])
        ans = 0
        for y in range(n):
            for x in range(m):
                mat[y][x] = int(mat[y][x])
                ans = max(mat[y][x], ans)
                if x - 1 < 0 or y - 1 < 0 or not mat[y][x]:
                    continue
                mat[y][x] = min(int(mat[y - 1][x]), int(mat[y - 1][x - 1]),
                                int(mat[y][x - 1])) + 1
                ans = max(mat[y][x], ans)
        return ans**2
