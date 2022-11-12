from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = 0
        for i, nr in enumerate(nums):
            if nums[i] == val:
                continue
            if nums[end] == val:
                nums[end], nums[i] = nums[i], nums[end]
            end += 1
        return end
