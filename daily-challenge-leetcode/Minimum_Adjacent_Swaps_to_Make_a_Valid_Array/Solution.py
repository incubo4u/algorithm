from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        lowest = float('inf')
        highest = -float('inf')
        hi , lo = 0,0
        for i, nr in enumerate(nums):
            if nr >= highest:
                highest = nr
                hi = i
            if nr < lowest:
                lowest = nr
                lo = i
        swaps = len(nums)-1 - hi
        swaps += lo - 1 if hi < lo else lo
        return swaps
