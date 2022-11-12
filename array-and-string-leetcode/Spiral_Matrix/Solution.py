from typing import List


class Solution:
    def spiralOrder(self, M: List[List[int]]) -> List[int]:
        h, w = len(M), len(M[0])
        ans = []
        i, j = 0, -1
        dir = 1
        while h * w > 0:
            for _ in range(w):
                j += dir
                ans.append(M[i][j])
            h -= 1
            for _ in range(h):
                i += dir
                ans.append(M[i][j])
            w -= 1
            dir *= -1
        return ans
