class Solution:

    def minimumLength(self, s: str) -> int:
        n = len(s)
        l = 0
        r = n - 1
        while l < r and s[l] == s[r]:
            left = s[l]
            right = s[r]
            while l < n and s[l] == right:
                l += 1
            while r >= 0 and s[r] == left:
                r -= 1
        return (r - l) + 1 if l <= r else 0
