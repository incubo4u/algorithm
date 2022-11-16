class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        if n < 3:
            return 1
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 1
        memo[3] = 2
        for i in range(4, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[n]
 