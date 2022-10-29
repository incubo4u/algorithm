from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        left, right = [0] * lenght, [0] * lenght
        left[0] = 1
        right[-1] = 1
        for i in range(1, lenght):
            left[i] = nums[i - 1] * left[i - 1]
        for i in reversed(range(lenght - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        for i in range(lenght):
            nums[i] = left[i] * right[i]
        return nums
