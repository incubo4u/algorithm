class Solution:

    def numberOfWays(self, s: str) -> int:
        n = len(s)
        n0 = n1 = n01 = n10 = n010 = n101 = 0
        for i in range(n):
            if s[i] == "1":
                n1 += 1
                n01 += n0
                n101 += n10
            else:
                n0 += 1
                n10 += n1
                n010 += n01
        return n101 + n010
