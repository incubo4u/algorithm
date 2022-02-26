from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        ret = []
        def sub(i):
            if i < len(nums):
                ret.append(nums[i])
                sub(i+1)
                ret.pop()
                sub(i+1)
            else:
                result.append(ret[:])

        sub(0)
        return result
