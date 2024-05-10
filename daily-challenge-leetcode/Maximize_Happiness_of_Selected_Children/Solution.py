class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(0, h - turn) for turn, h in enumerate(happiness[:k]))
