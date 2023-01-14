class UnionFind:

    def __init__(self, size=26):
        self.chars = list(range(size))

    def union(self, x, y):
        xi, yi = self.find(ord(x) - 97), self.find(ord(y) - 97)
        if xi == yi:
            return
        elif xi > yi:
            self.chars[xi] = yi
        else:
            self.chars[yi] = xi

    def find(self, x):
        if self.chars[x] == x:
            return x
        return self.find(self.chars[x])


class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        u = UnionFind()
        for _, (c1, c2) in enumerate(zip(s1, s2)):
            u.union(c1, c2)

        ans = []
        for c in baseStr:
            ans.append(chr(u.find(ord(c) - 97) + 97))
        return ''.join(ans)