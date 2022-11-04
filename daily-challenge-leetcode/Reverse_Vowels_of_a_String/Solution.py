class Solution:
    def reverseVowels(self, s: str) -> str:
        vowles = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while l < r and s[l] not in vowles:
                l += 1
            while r > l and s[r] not in vowles:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
