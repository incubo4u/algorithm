from collections import defaultdict
from functools import cache
from typing import List


class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        chars_per_pos = defaultdict(int)
        for w in words:
            for k, c in enumerate(w):
                chars_per_pos[(k, c)] += 1

        @cache
        def dp(t, w):
            if t > len(target) - 1:
                return 1
            if w > len(words[0]) - 1:
                return 0
            return dp(t, w + 1) + (dp(t + 1, w + 1) * chars_per_pos[(w, target[t])])

        return dp(0, 0) % 1000000007
