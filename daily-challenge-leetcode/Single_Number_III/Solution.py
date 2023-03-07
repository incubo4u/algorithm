class Solution:

    def singleNumber(self, nums):
        x = y = mask = 0
        for n in nums:
            mask ^= n
        right_bit = mask & -mask
        for n in nums:
            if n & right_bit:
                x ^= n
            else:
                y ^= n
        return x, y
