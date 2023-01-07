class Solution:

    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res |= ((n >> i) & 1) << (31 - i)
        return res