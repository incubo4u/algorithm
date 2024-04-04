class Solution:

    def maxDepth(self, s: str) -> int:
        ans = o = 0
        for char in s:
            o += int(char == "(") - int(char == ")")
            ans = max(ans, o)
        return ans
