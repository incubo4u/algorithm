from functools import cache


class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def roll(left, s):
            if s > target:
                return 0
            if left == 0:
                return int(s == target)
            ans = 0
            for i in range(1, k + 1):
                ans += roll(left - 1, s + i)
            return ans

        return roll(n, 0) % 1000000007
