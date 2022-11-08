from typing import Counter, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common()[0][0]
