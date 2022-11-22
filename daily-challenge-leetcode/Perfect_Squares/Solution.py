from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        def isPerfect(x):
            sqr = isqrt(x)
            if sqr * sqr == x:
                return True
            return False

        if isPerfect(n):
            return 1

        for i in range(1, isqrt(n) + 1):
            if i * i > n:
                break
            if isPerfect(n - i * i):
                return 2

        for i in range(1, isqrt(n) + 1):
            for j in range(i, isqrt(n) + 1):
                if i * i + j * j > n:
                    break
                if isPerfect(n - i * i - j * j):
                    return 3
        return 4
