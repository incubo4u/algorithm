from functools import cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)

        @cache
        def get_max(i, left):
            if i == m:
                return 0
            return max(
                nums[left] * multipliers[i] + get_max(i + 1, left + 1),
                nums[n - 1 - (i - left)] * multipliers[i] + get_max(i + 1, left),
            )

        return get_max(0, 0) 
