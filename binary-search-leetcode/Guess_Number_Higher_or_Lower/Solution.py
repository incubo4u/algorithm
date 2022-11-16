# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:
                r = mid - 1
            else:
                l = mid + 1
