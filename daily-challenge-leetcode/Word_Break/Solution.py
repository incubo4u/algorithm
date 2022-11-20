from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        W = set(wordDict)

        @cache
        def splt(i, j):
            if j >= len(s) - 1:
                return s[i : j + 1] in W
            if s[i : j + 1] in W:
                return splt(j + 1, j + 1) or splt(i, j + 1)
            else:
                return splt(i, j + 1)

        for i in range(len(s)):
            if (not i or s[:i] in W) and splt(i, i):
                return True
        return False
