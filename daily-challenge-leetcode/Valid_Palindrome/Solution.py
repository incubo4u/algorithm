import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = set(string.ascii_letters) | set(string.digits)
        s = [c.lower() for c in s if c in letters]
        return s == s[::-1]
