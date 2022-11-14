from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        x = min(nums)
        return set(range(x, x + len(nums))) == set(nums)
