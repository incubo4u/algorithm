from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for holding in range(2):
                do_nothing = dp[i + 1][holding]
                if holding:
                    do_sth = dp[i + 2][0] + prices[i]
                else:
                    do_sth = dp[i + 1][1] - prices[i]
                dp[i][holding] = max(do_nothing, do_sth)
        return dp[0][0]
