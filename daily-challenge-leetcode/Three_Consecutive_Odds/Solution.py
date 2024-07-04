# Runtime Percentile: 84.49369999999999
# Memory Percentile: 15.612799999999993


class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for n in arr:
            count = (count + (n % 2)) * (n % 2)
            if count == 3: return True
