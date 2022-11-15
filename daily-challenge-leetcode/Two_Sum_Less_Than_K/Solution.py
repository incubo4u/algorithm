from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        best = -1
        while l < r:
            s = nums[l] + nums[r]
            if s >= k:
                r -= 1
            else:
                l += 1
                best = max(s, best)

        return best
