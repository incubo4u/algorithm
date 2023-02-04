class Solution:

    def convert(self, s: str, r: int) -> str:
        if r < 2:
            return s
        c = [[] for _ in range(r)]
        s = list(s)
        h = -1
        for i in range(len(s)):
            if h + 1 > r - 1:
                d = -1
            elif h - 1 < 0:
                d = 1
            h += d
            c[h].append(s[i])
        ans = []
        for lvl in c:
            ans.extend(lvl)
        return ''.join(ans)