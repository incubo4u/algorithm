class Solution:

    def decodeString(self, s):
        n = len(s)
        ans, i = '', 0
        digit = 0
        while i < n:
            c = s[i]
            if c.isalpha():
                ans += c
            if c.isdigit():
                digit = digit * 10 + int(c)
            elif c == '[':
                chunck, end = self.decodeString(s[i + 1:])
                ans += chunck * digit
                digit = 0
                i += end
            elif c == ']':
                return ans, i + 1
            i += 1
        return ans
