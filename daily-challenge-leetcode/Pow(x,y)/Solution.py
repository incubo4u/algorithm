class Solution:

    def myPow(self, x: float, n: int) -> float:

        def mpow(x, n):
            if not n:
                return 1
            if n < 0:
                return 1 / mpow(x, -n)
            return mpow(x * x, n //
                        2) if not n % 2 else x * mpow(x * x, (n - 1) // 2)

        return mpow(x, n)
