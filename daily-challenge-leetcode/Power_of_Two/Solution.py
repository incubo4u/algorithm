class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & -(n) == n
        # return n & (n - 1) == 0
