from functools import cache
from typing import List


class Solution:

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len_one, len_two = len(nums1), len(nums2)

        @cache
        def count(o, t):
            if o > len_one - 1 or t > len_two - 1:
                return 0
            elif nums1[o] == nums2[t]:
                return count(o + 1, t + 1) + 1
            return max(count(o, t + 1), count(o + 1, t))

        return count(0, 0)
