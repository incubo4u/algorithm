from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, 100000):
            if i not in nums:
                return i
        return 100001