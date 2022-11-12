from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum, pivot = sum(nums), 0, -1
        for i in range(len(nums) - 1, -1, -1):
            rsum += nums[i + 1] if i + 1 < len(nums) else 0
            lsum -= nums[i]
            if lsum == rsum:
                pivot = i
        return pivot
