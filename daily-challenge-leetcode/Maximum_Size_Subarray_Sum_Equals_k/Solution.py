from typing import List


class Solution:

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        sums = {}
        for i, n in enumerate(nums):
            curr += n
            if curr == k:
                ans = max(i + 1, ans)
            if curr not in sums:
                sums[curr] = i
            if curr - k in sums and curr - (curr - k) == k:
                ans = max(abs(i - sums[curr - k]), ans)
        return ans
