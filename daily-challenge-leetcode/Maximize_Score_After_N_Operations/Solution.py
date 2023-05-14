from collections import defaultdict
from math import gcd
from typing import List


class Solution:

    def maxScore(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def backtrack(times, seen):
            if seen in cache:
                return cache[seen]
            for i in range(len(nums)):
                if 1 << i & seen:
                    continue
                for j in range(i + 1, len(nums)):
                    if 1 << j & seen:
                        continue
                    cache[seen] = max(
                        cache[seen], (gcd(nums[i], nums[j]) * times) +
                        backtrack(times + 1, seen | 1 << j | 1 << i))
            return cache[seen]

        return backtrack(1, 0)
