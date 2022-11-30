from functools import cache


class Solution:

    def isValidPalindrome(self, s: str, k: int) -> bool:

        @cache
        def check(l, r, k):
            if r - l + 1 <= 1:
                return True
            elif s[l] == s[r]:
                return check(l + 1, r - 1, k)
            elif k:
                return check(l + 1, r, k - 1) or check(l, r - 1, k - 1)
            return False

        return check(0, len(s) - 1, k)