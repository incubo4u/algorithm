from functools import cache


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        if n + m != l:
            return False

        @cache
        def check(i, j, k):
            if k > l - 1:
                return i > n - 1 and j > m - 1
            elif i > n - 1:
                return s2[j:] == s3[k:]
            elif j > m - 1:
                return s1[i:] == s3[k:]
            elif s3[k] == s1[i] != s2[j]:
                return check(i + 1, j, k + 1)
            elif s3[k] == s1[i] == s2[j]:
                return check(i + 1, j, k + 1) or check(i, j + 1, k + 1)
            elif s3[k] == s2[j] != s1[i]:
                return check(i, j + 1, k + 1)
            else:
                return False

        return check(0, 0, 0)
