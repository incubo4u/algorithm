class Solution:

    def toHex(self, num: int) -> str:
        if num < 0:
            num &= 0xffffffff
        if num == 0:
            return '0'
        h = "0123456789abcdef"
        ans = []
        while num:
            ans.append(h[num % 16])
            num //= 16
        return ''.join(reversed(ans))
