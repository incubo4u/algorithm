from typing import List


class Solution:

    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, s = len(nums), sum(nums)
        curr, ans = 10**5 + 1, 0
        left_s = 0
        for i, nr in enumerate(nums):
            left_s += nr
            right_s = s - left_s
            left_count = i + 1
            right_count = n - 1 - i if n - 1 - i > 0 else 1
            if (avg := abs((left_s // left_count) -
                          (right_s // right_count))) < curr:
                curr = avg
                ans = i
        return ans