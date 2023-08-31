from typing import List


class Solution:

    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        i = n - 1
        ans = 0
        right = nums[-1]
        while i >= 0:
            curr = nums[i]
            if curr > right:
                chunks = (curr + right - 1) // right
                ans += chunks - 1
                right = curr // chunks
            else:
                right = nums[i]
            i -= 1
        return ans
