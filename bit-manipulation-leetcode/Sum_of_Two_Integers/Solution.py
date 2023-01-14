class Solution:

    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < max_int else ~(a ^ mask)
