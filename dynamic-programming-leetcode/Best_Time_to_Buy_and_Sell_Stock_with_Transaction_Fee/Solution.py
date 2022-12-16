from typing import List


class Solution:

    def maxProfit(self, p: List[int], fee: int) -> int:
        cash = 0
        hold = -p[0]
        for i in range(1, len(p)):
            cash = max(cash, hold + p[i] - fee)
            hold = max(hold, cash - p[i])
        return cash
