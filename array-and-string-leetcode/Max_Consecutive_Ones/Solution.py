from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, best = 0, 0
        for r, n in enumerate(nums, 1):
            if n != 1:
                l = r
            else:
                best = max(r - l, best)
        return best
