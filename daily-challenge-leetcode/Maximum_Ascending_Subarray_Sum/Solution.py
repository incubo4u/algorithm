from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = ans = nums[0]
        for i, nr in enumerate(nums[1:], 1):
            if nums[i - 1] < nr:
                s += nr
            else:
                s = nr
            ans = max(ans, s)
        return ans
