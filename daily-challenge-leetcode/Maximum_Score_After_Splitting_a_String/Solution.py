class Solution:

    def maxScore(self, s: str) -> int:
        n = len(s)
        l = ans = 0
        r = s.count("1")
        for i in range(n - 1):
            l += int(s[i] == "0")
            r -= int(s[i] == "1")
            ans = max(l + r, ans)
        return ans
