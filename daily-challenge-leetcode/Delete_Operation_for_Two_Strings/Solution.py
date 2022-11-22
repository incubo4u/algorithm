class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l_one, l_two = len(word1), len(word2)
        dp = [[0 for _ in range(l_two + 1)] for _ in range(l_one + 1)]
        for i, o in enumerate(word1, 1):
            for j, t in enumerate(word2, 1):
                if t == o:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return (l_one + l_two) - (dp[-1][-1] * 2)
