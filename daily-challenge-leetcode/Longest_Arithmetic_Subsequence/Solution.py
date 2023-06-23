from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        result = 0
        for i in range(n):
            for j in range(0, i):
                key = i, (diff := nums[i] - nums[j])
                dp[key] = max(dp[(j, diff)] + 1, dp[key])
                result = max(result, dp[key])

        return result + 1
