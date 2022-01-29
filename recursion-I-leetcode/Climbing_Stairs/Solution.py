class Solution:
    def climbStairs(self, n: int) -> int:
        results = {}
        def climb_rec(n: int) -> int:
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n not in results:
                results[n] = climb_rec(n-1) + climb_rec(n-2)
            return results[n]
        return climb_rec(n)