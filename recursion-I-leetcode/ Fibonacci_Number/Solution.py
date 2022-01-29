from typing import int
class Solution:
    def fib(self,n: int) -> int:
        results = {}
        def fib_rec(n: int) -> int:
            if n == 1:
                return 1
            if n == 0:
                return 0
            if n in results:
                return results[n]
            results[n] = fib_rec(n-1) + fib_rec(n-2)
            return results[n]
        return fib_rec(n)