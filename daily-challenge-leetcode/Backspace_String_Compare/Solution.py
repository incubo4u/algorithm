class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S,T = list(s),list(t)
        s,t = [],[]
        for c in S:
            if c =='#' :
                if s : s.pop()
            else:
                s.append(c)
        for c in T:
            if c =='#':
                if t : t.pop()
            else:
                t.append(c)
        return s == t