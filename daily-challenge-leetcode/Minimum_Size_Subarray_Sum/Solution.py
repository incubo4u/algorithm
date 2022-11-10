from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        ans = float("inf")

        for right, nr in enumerate(nums):
            curr_sum += nr

            while curr_sum - nums[left] >= target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum >= target:
                ans = min(ans, (right - left) + 1)
        return ans if ans != float("inf") else 0
