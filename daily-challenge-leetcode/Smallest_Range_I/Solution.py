from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        hi, lo = (max(nums) - k), (min(nums) + k)
        diff = hi - lo
        return diff if diff > 0 else 0
