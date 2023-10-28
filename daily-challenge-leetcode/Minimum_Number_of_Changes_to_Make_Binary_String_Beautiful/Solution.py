class Solution:

    def minChanges(self, s: str) -> int:
        return sum((int(s[i - 1] != s[i - 2]) for i in range(2,
                                                             len(s) + 1, 2)))
