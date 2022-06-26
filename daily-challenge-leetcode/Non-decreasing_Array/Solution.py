from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        i = 0
        replaced = 1
        lastMax = 0
        while i < len(nums) - 1 and replaced >= 0:
            if nums[i] > nums[i + 1]:
                if lastMax <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                replaced -= 1
            i += 1
            lastMax = nums[i - 1]
        if replaced >= 0:
            return True
        return False
