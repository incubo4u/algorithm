from functools import cache


class Solution:

    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)

        @cache
        def jump(i, jp, k):
            if i == n - 1:
                return jp == stones[i]
            if stones[i] > jp:
                return
            elif stones[i] < jp:
                return jump(i + 1, jp, k)
            else:
                return (jump(i + 1, jp + k - 1, k - 1)
                        or jump(i + 1, jp + k + 1, k + 1)
                        or jump(i + 1, k + jp, k))

        return jump(0, 1, 1)
