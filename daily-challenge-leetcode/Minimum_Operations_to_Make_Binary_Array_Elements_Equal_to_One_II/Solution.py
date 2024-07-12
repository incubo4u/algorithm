# Runtime Percentile: 47.19139999999997
# Memory Percentile: 76.37920000000004


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = flips = 0
        flipped = 0
        for i, n in enumerate(nums):
            if (not n and not flipped) or (n and flipped):
                flipped = not flipped
                ans += 1
        return ans
