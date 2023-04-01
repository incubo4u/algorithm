from collections import Counter
from functools import cache


class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:

        @cache
        def f(one, two):
            n = len(one)
            if one == two:
                return True
            if Counter(one) != Counter(two):
                return
            for i in range(1, n):
                if f(one[:i], two[:i]) and f(one[i:], two[i:]):
                    return True
                if f(one[:i], two[n - i:]) and f(one[i:], two[:n - i]):
                    return True

        return f(s1, s2)
