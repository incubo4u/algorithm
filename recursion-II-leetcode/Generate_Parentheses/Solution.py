
class Solution(object):
    def generateParenthesis(self, n):
        result = []
        sub = []
        maxLen = n*2
        def gen(open, close):
            if len(sub) < maxLen:
                if close < open:
                    sub.append(')')
                    gen(open, close+1)
                    sub.pop()
                sub.append('(')
                gen(open+1, close)
                sub.pop()
            else:
                if open == close:
                    result.append(''.join(sub))
        gen(0, 0)
        return result