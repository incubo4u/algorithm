class Solution:

    def longestSubarray(self, nums: list[int]) -> int:
        z = ans = o = t = 0
        for n in nums:
            if n:
                o += 1
            else:
                z = 1
                ans = max(ans, o + t)
                t = o
                o = 0
        return max(ans, o - 1 if not z else o + t)
