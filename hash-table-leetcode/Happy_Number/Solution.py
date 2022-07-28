from functools import lru_cache


class Solution:
    def isHappy(self, n: int) -> bool:
        nr = map(int, str(n))

        @lru_cache
        def squares(n):
            return n**2

        s = 0
        cycle = set()
        while s != '1':
            s = str(sum(map(squares, nr)))
            if s in cycle:
                break
            nr = map(int, s)
            cycle.add(s)

        return s == '1'