from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = Counter(nums1) & Counter(nums2)
        return [ nr for nr , freq in intersection.items() for _ in range(freq)]
