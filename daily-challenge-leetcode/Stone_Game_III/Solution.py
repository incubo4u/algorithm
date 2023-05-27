from functools import cache


class Solution:
    def stoneGameIII(self, piles: list[int]) -> str:
        n = len(piles)
        INF = 10**10

        @cache
        def play(i):
            if i > n - 1:
                return 0
            best = -INF
            curr = 0
            for j in range(1, 4):
                if j + i - 1 > n - 1:
                    break
                curr += piles[i + j - 1]
                best = max(best, curr - play(i + j))
            return best

        winner = play(0)
        if winner > 0:
            return "Alice"
        elif winner < 0:
            return "Bob"
        return "Tie"
