from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        for c in tokens:
            if c in ('-', '+', '*', '/'):
                stack.append(op[c](b=stack.pop(), a=stack.pop()))
            else:
                stack.append(int(c))
        return stack.pop()