class Solution:

    def countSubmatrices(self, g: List[List[int]], k: int) -> int:
        n, m = len(g), len(g[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                up = g[i - 1][j] if i - 1 >= 0 else 0
                left = g[i][j - 1] if j - 1 >= 0 else 0
                corner = g[i - 1][j - 1] if j - 1 >= 0 and i - 1 >= 0 else 0
                g[i][j] += up + left - corner
                if g[i][j] > k:
                    break
                ans += 1
        return ans
