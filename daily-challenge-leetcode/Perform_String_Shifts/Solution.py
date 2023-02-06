from typing import List


class Solution:

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sf = 0
        n = len(s)
        direction = (1, -1)
        for d, amount in shift:
            sf += direction[d] * amount
        sf %= n
        if sf > 0:
            return s[sf:] + s[:sf]
        return s