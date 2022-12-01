class Solution:

    def isPalindrome(self, x: int) -> bool:
        return (sx := str(x)) == sx[::-1]