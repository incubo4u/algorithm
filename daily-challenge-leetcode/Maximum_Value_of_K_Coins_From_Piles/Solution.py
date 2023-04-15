from typing import List
from functools import cache


class Solution:

    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
        n = len(piles)

        @cache
        def take(k, i):
            if not k or i > n - 1:
                return 0
            best = take(k, i + 1)
            curr = 0
            for j in range(min(k, len(piles[i]))):
                curr += piles[i][j]
                best = max(curr + take(k - j - 1, i + 1), best)
            return best

        return take(K, 0)
