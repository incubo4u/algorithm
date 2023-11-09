class Solution:

    def countHomogenous(self, s: str) -> int:
        mod = (10**9) + 7
        ans = sub_len = l = 0
        for r, c in enumerate(s):
            sub_len = 1 + (sub_len * int(s[l] == c))
            l = r * int(s[l] != c) + l * int(s[l] == c)
            ans += sub_len
        return ans % mod
