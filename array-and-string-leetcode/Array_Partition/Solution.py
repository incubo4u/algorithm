from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(nr for i, nr in enumerate(sorted(nums)) if i % 2 == 0)
