class Solution:

    def longestValidParentheses(self, s: str) -> int:
        best = 0
        stack = [-1]
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
                continue
            stack.pop()
            if stack:
                best = max(i - stack[-1], best)
            else:
                stack.append(i)
        return best
