class Solution:
    def reverse(self, x: int) -> int:
        upper_bound = 2147483647
        lower_bound = -2147483648
        neg = False
        sx = str(x)
        if sx[0] == "-":
            neg = True
            sx = sx[1:]
        x = int(sx[::-1])
        if neg:
            x = -x
        if lower_bound <= x <= upper_bound:
            return x
        return 0
