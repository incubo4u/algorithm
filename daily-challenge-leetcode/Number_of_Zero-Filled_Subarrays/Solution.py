from typing import List


class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = ans = 0
        for r, n in enumerate(nums):
            if not n:
                ans += 1
            if not n and not nums[l]:
                ans += r - l
            else:
                l = r
        return ans