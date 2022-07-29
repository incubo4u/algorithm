from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        h = {}
        for i, nr in enumerate(nums):
            if nr not in h:
                h[nr] = [i]
            else:
                for j, n in enumerate(h[nr]):
                    if abs(n - i) <= k:
                        return True
                h[nr].append(i)
        return False
