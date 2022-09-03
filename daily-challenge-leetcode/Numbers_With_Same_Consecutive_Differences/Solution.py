from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ret = []

        def backtrack(nr):

            if len(nr) == n:
                ret.append("".join(str(x) for x in nr))
                return

            for i in range(10):
                if not nr and i == 0:
                    continue
                if not nr or abs(nr[-1] - i) == k:
                    nr.append(i)
                    backtrack(nr)
                    nr.pop()

        backtrack([])
        return ret
