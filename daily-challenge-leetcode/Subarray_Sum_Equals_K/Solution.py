from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if k == nums[0] else 0
        d = defaultdict(list)
        ret, curr = 0, 0
        for i, nr in enumerate(nums):
            curr += nr
            if curr == k:
                ret += 1
            if curr - k in d:
                ret += len(d[curr - k])
            d[curr].append(i)

        return ret
