class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        # alph = [0]*26
        # for c in s:
        #     alph[ord(c) - 97]+=1
        # for c in t:
        #     alph[ord(c) - 97]-=1
        #     if alph[ord(c) - 97] < 0 : return c
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
