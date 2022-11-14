from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shiftChar(c, shift):
            new_c = (ord(c) - 96 + shift) % 26
            if new_c == 0:
                new_c = 26
            return chr((new_c + 96))

        shift_sum = 0
        ans = []
        for i, (c, shift) in enumerate(zip(reversed(s), reversed(shifts))):
            shift_sum += shift
            ans.append(shiftChar(c, shift_sum))
        return "".join(reversed(ans))
