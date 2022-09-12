from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        tokens.sort()
        score, best = 0, 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                best = max(best, score)
                l += 1
            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break

        return best
