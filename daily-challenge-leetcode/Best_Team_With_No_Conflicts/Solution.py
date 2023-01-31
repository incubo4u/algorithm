from typing import List


class Solution:

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        p = sorted(zip(scores, ages))
        dp = [0] * (max(ages) + 1)
        for _, (score, age) in enumerate(p):
            dp[age] = max(dp[:age + 1]) + score
        return max(dp)
