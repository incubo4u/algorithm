from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            i, j, count = 0, 1, 0
            while i < len(nums):
                # distance = nums[j] - nums[i]
                while j < len(nums) and nums[j] - nums[i] <= guess:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low
