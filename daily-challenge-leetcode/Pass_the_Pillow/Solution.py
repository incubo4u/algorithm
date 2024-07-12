# Runtime Percentile: 59.2405
# Memory Percentile: 77.72139999999999


class Solution:

    def passThePillow(self, n: int, time: int) -> int:
        q, rem = divmod(time, n - 1)
        if q % 2: return n - rem
        return rem + 1
