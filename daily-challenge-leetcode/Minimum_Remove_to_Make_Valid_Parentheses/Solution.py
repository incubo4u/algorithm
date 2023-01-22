from string import ascii_lowercase


class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rm = set()
        for i, c in enumerate(s):
            if c in ascii_lowercase:
                continue
            elif c == '(':
                stack.append((c, i))
            elif stack and c == ')' and stack[-1][0] == '(':
                stack.pop()
            else:
                rm.add(i)
        rm |= set(map(lambda e: e[1], stack))
        return [c for i, c in enumerate(s) if i not in rm]
