from functools import cache


class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def check(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return check(l + 1, r - 1) + 2
            return max(check(l + 1, r), check(l, r - 1))

        return check(0, len(s) - 1)
