class Solution:
    def makeGood(self, s: str) -> str:
        def toRemove(f, s):
            return (
                (f.islower() and s.isupper()) or (f.isupper() and s.islower())
            ) and f.lower() == s.lower()

        i, j = 0, 1
        while j < len(s):
            if toRemove(s[i], s[j]):
                s = s[:i] + s[j + 1 :]
                i = i - 1 if i - 1 >= 0 else 0
                j = i + 1
                continue
            i += 1
            j += 1
        return s
