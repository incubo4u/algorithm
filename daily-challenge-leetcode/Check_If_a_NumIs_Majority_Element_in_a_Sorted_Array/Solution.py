from bisect import bisect_left, bisect_right


class Solution:

    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        return bisect_right(nums, target) - bisect_left(nums, target) > n // 2
