from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                w = len(word)
                if i >= w - 1 and (i == w - 1 or dp[i - (w - 1) - 1]):
                    if s[i - (w - 1):i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]