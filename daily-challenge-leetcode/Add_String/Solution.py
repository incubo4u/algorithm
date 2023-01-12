class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        ni, mi = len(num1) - 1, len(num2) - 1
        ans = []
        carry = 0
        while ni >= 0 or mi >= 0:
            n = m = 0
            if ni >= 0:
                n = ord(num1[ni]) - ord('0')
            if mi >= 0:
                m = ord(num2[mi]) - ord('0')
            s = n + m + carry
            ans.append(str(s % 10))
            carry = s // 10
            ni -= 1
            mi -= 1
        if carry:
            ans.append(str(carry))
        return ''.join(reversed(ans))
