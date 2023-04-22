from functools import cache


class Solution:

    def minInsertions(self, s: str) -> int:

        @cache
        def check(l, r):
            if l >= r:
                return 0
            if s[l] != s[r]:
                return min(check(l + 1, r) + 1, check(l, r - 1) + 1)
            return check(l + 1, r - 1)

        return check(0, len(s) - 1)
