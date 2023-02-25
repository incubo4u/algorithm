from functools import cache


class Solution:

    def numberOfWays(self, m: int) -> int:
        mod = 10**9 + 7

        @cache
        def count(n):
            if 0 >= n:
                return 1
            elif n % 2:
                return 1
            elif n == 2:
                return 1
            else:
                ans = 0
                for l in range(0, n, 2):
                    r = n - l - 2
                    ans += count(l) * count(r)
                return ans

        return count(m) % mod
