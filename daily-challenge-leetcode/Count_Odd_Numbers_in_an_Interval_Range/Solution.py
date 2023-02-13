from math import ceil


class Solution:
    def countOdds(self, low: int, high: int) -> int:

        return ceil((high - low) / 2) + 1 if low % 2 and high % 2 else ceil((high - low) / 2)