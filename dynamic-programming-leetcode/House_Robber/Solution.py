from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])
        return memo[-1] 
