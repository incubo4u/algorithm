class Solution:
    def climbStairs(self, n: int) -> int:
        # results = {}
        # def climb_rec(n: int) -> int:
        #     if n < 2:
        #         return 1
        #     if n not in results:
        #         results[n] = climb_rec(n-1) + climb_rec(n-2)
        #     return results[n]
        # return climb_rec(n)
        if n < 2:
            return 1
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]
        return memo[n]
