from typing import List


class Solution:

    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        # @cache
        # def paint(home, color):
        #     if home > n - 1:
        #         return 0
        #     elif color == 0:
        #         return min(
        #             paint(home + 1, 1) + costs[home][1],
        #             paint(home + 1, 2) + costs[home][2])
        #     elif color == 1:
        #         return min(
        #             paint(home + 1, 0) + costs[home][0],
        #             paint(home + 1, 2) + costs[home][2])
        #     else:
        #         return min(
        #             paint(home + 1, 0) + costs[home][0],
        #             paint(home + 1, 1) + costs[home][1])

        # return min(map(lambda c: paint(0, c), (0, 1, 2)))

        dp = [[0] * 3 for i in range(n)]
        dp[0] = costs[0]
        for home in range(1, n):
            for color in range(3):
                if color == 0:
                    dp[home][color] = min(dp[home - 1][1],
                                          dp[home - 1][2]) + costs[home][color]
                elif color == 1:
                    dp[home][color] = min(dp[home - 1][0],
                                          dp[home - 1][2]) + costs[home][color]
                else:
                    dp[home][color] = min(dp[home - 1][0],
                                          dp[home - 1][1]) + costs[home][color]
        return min(dp[-1])
