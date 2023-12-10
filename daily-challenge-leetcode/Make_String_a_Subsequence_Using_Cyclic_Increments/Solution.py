class Solution:

    def canMakeSubsequence(self, one: str, two: str) -> bool:
        t = 0
        for o, co in enumerate(one):
            same = co == (ct := two[t])
            same_after_inc = (ord(co) - ord('a') +
                              1) % 26 == ord(ct) - ord('a')
            if same or same_after_inc:
                t += 1
            if t == len(two):
                return True
        return
