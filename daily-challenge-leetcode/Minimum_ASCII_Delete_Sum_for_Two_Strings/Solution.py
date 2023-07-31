from functools import cache


class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        INF = 10**8

        @cache
        def getmin(i, j):
            if s1[i:] == s2[j:]:
                return 0

            ans = INF
            if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                ans = getmin(i + 1, j + 1)

            if i < len(s1):
                ans = min(getmin(i + 1, j) + ord(s1[i]), ans)

            if j < len(s2):
                ans = min(getmin(i, j + 1) + ord(s2[j]), ans)

            return ans

        return getmin(0, 0)
