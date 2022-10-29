from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seq = 0
        best_seq = 0
        before_zero = 0
        flip = False
        for nr in nums:
            if nr == 1:
                seq += 1
                before_zero += 1
            elif not flip:
                seq += 1
                before_zero = 0
                flip = True
            else:
                seq = before_zero + 1
                before_zero = 0
            best_seq = max(best_seq, seq)
        return best_seq
