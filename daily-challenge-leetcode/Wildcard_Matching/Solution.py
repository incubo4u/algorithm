from functools import cache


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        str_lenght = len(s)
        pattern_lenght = len(p)

        @cache
        def match(i, pi) -> bool:
            if i > str_lenght - 1:
                while pi < pattern_lenght and p[pi] == '*':
                    pi += 1
                return pi > pattern_lenght - 1
            elif pi > pattern_lenght - 1:
                return
            res = False
            if p[pi] == '*':
                res = match(i + 1, pi + 1) or match(i + 1, pi) or match(
                    i, pi + 1)
            elif p[pi] == '?' or p[pi] == s[i]:
                res = match(i + 1, pi + 1)
            return res

        return match(0, 0)
