from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, nr in enumerate(nums):
            h[nr] = i
        for i, nr in enumerate(nums):
            c = target - nr
            if c in h and h[c] != i:
                return [i, h[c]]
