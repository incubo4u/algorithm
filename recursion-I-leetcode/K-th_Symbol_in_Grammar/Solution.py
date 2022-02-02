import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        flipAmount = 0
        rootVal = False

        def kthRec(n, k):
            nonlocal flipAmount
            if n == 1 or k == 1:
                return
            if k % 2 == 0:
                flipAmount += 1
            kthRec(n-1, math.ceil(k/2))
        kthRec(n, k)
        rootVal = not rootVal if flipAmount % 2 == 1 else rootVal
        return int(rootVal)
