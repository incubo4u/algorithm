from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**20

        for i in range(n):
            l, r = i + 1, n - 1
            t = target - nums[i]

            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if abs(best - target) > abs(s - target):
                    best = s
                if s - nums[i] > t:
                    r -= 1
                else:
                    l += 1
        return best
