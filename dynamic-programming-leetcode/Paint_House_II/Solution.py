from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n,k = len(costs),len(costs[0])
        dp = [ [0] * k for i in range(n) ]
        dp[0] = costs[0]
        for home in range(1,n):
            for color in range(k):
                dp[home][color] = min(dp[home-1][:color]+dp[home-1][color+1:]) + costs[home][color]
        return min(dp[-1])
        