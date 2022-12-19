from functools import cache


class Solution:

    def numTilings(self, n: int) -> int:

        @cache
        def partial(k):
            if k == 2:
                return 1
            return partial(k - 1) + full(k - 2)

        @cache
        def full(k):
            if k <= 2:
                return k
            return full(k - 1) + full(k - 2) + (2 * partial(k - 1))

        return full(n) % 1_000_000_007