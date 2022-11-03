from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def comb(i, sub):
            if len(sub) == k:
                ans.append(sub.copy())
                return
            for j in range(i, n + 1):
                sub.add(j)
                comb(j + 1, sub)
                sub.remove(j)

        comb(1, set())
        return ans
