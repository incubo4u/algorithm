from typing import List


class Solution:
    def maxArea(self, H: List[int]) -> int:
        l, r = 0, len(H) - 1
        area = 0
        while l < r:
            area = max(area, min(H[l], H[r]) * (r - l))
            if H[l] > H[r]:
                r -= 1
            else:
                l += 1
        return area
