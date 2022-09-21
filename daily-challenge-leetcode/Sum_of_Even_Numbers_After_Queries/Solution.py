from typing import List


class Solution:
    def sumEvenAfterQueries(self, N: List[int], Q: List[List[int]]) -> List[int]:
        ret = []
        s = sum(n for i, n in enumerate(N) if n % 2 == 0)
        for _, (val, i) in enumerate(Q):
            if N[i] % 2 == 0:
                s -= N[i]
            N[i] += val
            if N[i] % 2 == 0:
                s += N[i]
            ret.append(s)
        return ret
