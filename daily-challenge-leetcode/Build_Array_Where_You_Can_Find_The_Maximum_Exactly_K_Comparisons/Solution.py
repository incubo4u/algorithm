class Solution:

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = (10**9) + 7

        @cache
        def count(rem, k, mx):
            if k < 0:
                return 0
            
            if not rem:
                return 1 * int(not k)

            ans = 0
            if k > 0:
                for bigger in range(mx + 1, m + 1):
                    ans += count(rem - 1, k - 1, bigger)

            for smaller in range(1, mx + 1):
                ans += count(rem - 1, k, mx)

            return ans % mod

        return count(n, k, 0) % mod
