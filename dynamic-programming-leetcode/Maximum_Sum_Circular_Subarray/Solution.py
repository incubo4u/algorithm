from typing import List


class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        INF, s = 30000, 0
        curr_b = best = -INF
        curr_w = worst = INF

        for i, n in enumerate(nums):
            s += n
            curr_b = max(curr_b + n, n)
            curr_w = min(curr_w + n, n)
            best = max(curr_b, best)
            worst = min(curr_w, worst)
        if s == worst:
            return best
        return max(s - worst, best)
