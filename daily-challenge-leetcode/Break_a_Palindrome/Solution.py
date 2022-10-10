class Solution:
    def breakPalindrome(self, P: str) -> str:
        if len(P) == 1:
            return ""
        replace = -1
        for i in range(len(P) // 2):
            if P[i] != "a":
                replace = i
                break
        else:
            return P[: len(P) - 1] + "b"
        return P[:i] + "a" + P[i + 1 :]
