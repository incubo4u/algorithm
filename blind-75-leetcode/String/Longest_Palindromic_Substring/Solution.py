class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s
        else:
            maxlen = 1
            start = 0

            for i in range(1, len(s)):
                odd = s[i - 1 - maxlen : i + 1]
                even = s[i - maxlen : i + 1]

                if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                    start = i - 1 - maxlen
                    maxlen = maxlen + 2
                    continue

                if even == even[::-1]:
                    start = i - maxlen
                    maxlen = maxlen + 1
        return s[start : start + maxlen]

