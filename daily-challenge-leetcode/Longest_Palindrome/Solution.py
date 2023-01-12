from collections import Counter


class Solution:

    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = carry = 0
        for freq in counter.values():
            ans += (freq // 2) * 2
            carry += freq % 2
        if carry:
            ans += 1
        return ans