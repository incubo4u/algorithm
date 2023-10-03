class Solution:

    def numIdenticalPairs(self, nums: list[int]) -> int:
        seen = [0] * 101
        ans = 0
        for n in nums:
            ans += seen[n]
            seen[n] += 1
        return ans
