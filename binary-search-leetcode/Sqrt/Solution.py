class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        mid = (left + right) // 2
        while left < right:
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
        return left - 1

