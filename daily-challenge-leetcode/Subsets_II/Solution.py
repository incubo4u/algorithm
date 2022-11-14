from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        nums.sort()

        def backtrack(i, subset):
            counter = tuple(Counter(subset).items())
            if counter in seen:
                return
            seen.add(counter)
            result.append(subset)
            for j in range(i, len(nums)):
                backtrack(j + 1, subset + [nums[j]])

        backtrack(0, [])
        return result
