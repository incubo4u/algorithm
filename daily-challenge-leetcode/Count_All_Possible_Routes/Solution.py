from functools import cache


class Solution:
    def countRoutes(self, loc: list[int], start: int, finish: int, fuel: int) -> int:
        n = len(loc)

        @cache
        def dp(i, f):
            return sum(
                dp(j, new_f)
                for j in range(n)
                if i != j and (new_f := f - abs(loc[i] - loc[j])) >= 0
            ) + int(i == finish)

        mod = (10**9) + 7
        return dp(start, fuel) % mod
