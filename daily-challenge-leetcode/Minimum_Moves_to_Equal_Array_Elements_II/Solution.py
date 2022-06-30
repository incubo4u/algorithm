from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        score = 0
        nums.sort()
        median = nums[len(nums) // 2]
        for nr in nums:
            score += abs(nr - median)
        return score

