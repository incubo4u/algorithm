from typing import List


class Solution:
    def trap(self, H: List[int]) -> int:
        divide = H.index(max(H))
        H_one = H[: divide + 1]
        H_two = H[divide:][::-1]
        result = 0

        def get_water(H):
            while H and H[0] < 1:
                H.pop(0)
            if not H:
                return
            nonlocal result
            last_h, last_index = H[0], 0
            for i, curr_h in enumerate(H):
                if curr_h < last_h:
                    continue
                result += sum(map(lambda h: last_h - h, H[last_index + 1 : i]))
                last_h, last_index = curr_h, i

        get_water(H_one)
        get_water(H_two)

        return result
