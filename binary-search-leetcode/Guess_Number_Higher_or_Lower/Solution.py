# The guess API is already defined for you.
# @param mid, your guess
# @return -1 if mid is higher than the picked number
#          1 if mid is lower than the picked number
#          otherwise return 0
import time

def guess(mid: int) -> int:
    picked = 3
    if mid == picked:
        return 0
    if mid > picked:
        return -1
    return 1


class Solution:
    def guessNumber(self, n) -> int:
        if n == 2:
            return 2
        left = 1
        right = n
        mid = (left + right) // 2
        result = guess(mid)
        while left < right:
            if result == 1:
                left = mid + 1
            else:
                right = mid 
            mid = (left + right) // 2
            result = guess(mid)
        if result == 0:
            return mid
        else:
            return left - 1


s = Solution()
print(s.guessNumber(3))
