from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            ret = []
            while left and right:
                if left[0] < right[0]:
                    ret.append(left[0])
                    left.remove(left[0])
                else:
                    ret.append(right[0])
                    right.remove(right[0])
            if left:
                ret.extend(left)
            else:
                ret.extend(right)
            return ret
        if len(nums) == 1:
            return nums
        cut = len(nums)//2
        left = self.sortArray(nums[0:cut])
        right = self.sortArray(nums[cut:])
        nums = merge(left, right)
        return nums
