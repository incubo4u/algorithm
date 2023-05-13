from functools import cache


class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = (10**9) + 7

        @cache
        def backtrack(comb_len):
            if comb_len > high:
                return 0
            elif comb_len == high:
                return 1
            ret = backtrack(comb_len + zero) + backtrack(comb_len + one)
            if low <= comb_len <= high:
                ret += 1
            return ret % mod

        return backtrack(0)