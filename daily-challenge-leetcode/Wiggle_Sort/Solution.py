from typing import List


class Solution:

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
