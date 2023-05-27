from functools import cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        INF = 10**10

        @cache
        def play(i, available_moves):
            if i > n - 1:
                return 0
            curr = 0
            best = -INF
            for j in range(1, 2 * available_moves + 1):
                if i + j - 1 > n - 1:
                    break
                curr += piles[j + i - 1]
                best = max(curr - play(j + i, max(j, available_moves)), best)
            return best

        return (sum(piles) + play(0, 1)) // 2
