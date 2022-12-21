class Solution:

    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = []
        if num < 0:
            ans.append('-')
        num = abs(num)
        while num > 0:
            ans.append(str(num % 7))
            num //= 7
        return ''.join(reversed(ans))
