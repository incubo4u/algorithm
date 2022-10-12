from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        lenght = len(nums)
        nums.sort()
        for i in range(lenght - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
