class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)
        n = n[2:]
        return int(n[::-1] + "0" * (32 - len(n)), 2)
