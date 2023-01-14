class Solution:

    def findRepeatedDnaSequences(self, s: str):
        ans = set()
        if (n := len(s)) < 10:
            return ans
        seen = set()
        for i in range(n):
            if (seq := s[i:i + 10]) in seen:
                ans.add(seq)
            else:
                seen.add(seq)
        return ans
