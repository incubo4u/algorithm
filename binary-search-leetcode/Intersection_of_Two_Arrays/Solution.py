from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = set(nums1)
        two = set(nums2)
        return one.intersection(two)