from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = { nr: i for i, nr in enumerate(nums2) }
        for i, nr in enumerate(nums1):
            nums1[i] = indexes[nr]
        return nums1