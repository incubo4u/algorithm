from typing import List


class Solution:

  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1]      * (amount + 1)
    dp[0] = 0
    for i in range(1, len(dp)):
      for m in coins:
        if i - m >= 0:
          dp[i] = min(dp[i - m] + 1, dp[i])
    return dp[-1] if dp[-1] != amount + 1 else -1
