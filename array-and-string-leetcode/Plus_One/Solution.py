from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, digits = 0, [0] + digits
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if carry > 0:
                digits[i] += carry
                carry = 0
            if digits[i] >= 10:
                nr = digits[i]
                digits[i] %= 10
                carry += nr // 10
            else:
                break
        return digits if digits[0] > 0 else digits[1:]
