from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        last_largest, largest, l = -1, -1, -1
        for i, nr in enumerate(nums):
            if nr >= largest:
                l, largest, last_largest = i, nr, largest
            elif nr >= last_largest:
                last_largest = nr
        if largest >= last_largest * 2:
            return l
        return -1
