class Solution:
    def calculate(self, s: str) -> int:
        ans, curr, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                curr = (curr * 10) + int(c)

            elif c == "-":
                ans += curr * sign
                curr = 0
                sign = -1

            elif c == "+":
                ans += curr * sign
                curr = 0
                sign = 1

            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                sign = 1
                ans = 0

            elif c == ")":
                ans += sign * curr
                ans *= stack.pop()
                ans += stack.pop()
                curr = 0

        return ans + curr * sign
