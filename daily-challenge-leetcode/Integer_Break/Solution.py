class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        ans = 1
        while n != 4 and n != 2 and n != 0:
            n -= 3
            ans *= 3
        if n > 0:
            ans *= n
        return ans
# 2 < e < 3

