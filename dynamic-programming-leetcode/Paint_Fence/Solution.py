class Solution:

    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        fence = [0] * (n)
        fence[0] = k
        fence[1] = k * k
        for i in range(2, n):
            fence[i] = (fence[i - 1] + fence[i - 2]) * (k - 1)
        return fence[-1]