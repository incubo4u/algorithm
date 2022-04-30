# from functools import lru_cache
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
        
        # @lru_cache(maxsize=5)
        # def fib_lru(self,n:int) -> int:
        #     if n == 1:
        #         return 1
        #     if n == 0:
        #         return 0 
        #     return fib_lru(n-1) + fin_lru(n+1)
