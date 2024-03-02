class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count("1")
        zero = n - ones
        return "1" * (ones - 1) + "0" * zero + "1"
