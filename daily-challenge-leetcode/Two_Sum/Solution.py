from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {k: v for v, k in enumerate(nums)}
        for i, nr in enumerate(nums):
            need = target - nr
            if need in d and d[need] != i:
                return [i, d[need]]
