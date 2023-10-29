class Solution:

    def longestPalindrome(self, s: str) -> str:
        best_length = 1
        ans = (0, 1)
        n = len(s)

        def findPalindorme(l, r):
            while l - 1 >= 0 and r < n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + int(s[l] != s[r]), r + int(s[l] == s[r])

        for i in range(n - 1):
            l, r = findPalindorme(i, i)
            if r - l > best_length:
                best_length = r - l
                ans = l, r

            l, r = findPalindorme(i, i + 1)
            if r - l > best_length:
                best_length = r - l
                ans = l, r

        return s[ans[0]:ans[1]]
