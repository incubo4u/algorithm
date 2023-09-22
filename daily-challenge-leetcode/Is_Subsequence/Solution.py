class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        for c in t:
            if i > n - 1:
                break
            i += int(c == s[i])
        return i > n - 1
