from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        sub = []
        n += 1

        def comb(i):
            if i <= n:
                if len(sub) < k:
                    sub.append(i)
                    comb(i+1)
                    sub.pop()
                    comb(i+1)
                else:
                    result.append(sub[:])
