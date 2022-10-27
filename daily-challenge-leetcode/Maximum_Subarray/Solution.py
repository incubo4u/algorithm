from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        for i , nr in enumerate(nums[1:],1):
            nums[i] = max(nr+nums[i-1],nr)
            best = max(best,nums[i])
        return best