class UnionFind:

    def __init__(self, size):
        self.islands = [i for i in range(size)]
        self.rank = [0] * size

    def connect(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi:
            return 0
        elif self.rank[xi] > self.rank[yi]:
            self.islands[yi] = xi
        elif self.rank[xi] < self.rank[yi]:
            self.islands[xi] = yi
        else:
            self.islands[xi] = yi
            self.rank[yi] += 1
        return 1

    def find(self, x):
        if self.islands[x] == x:
            return x
        self.islands[x] = self.find(self.islands[x])
        return self.islands[x]


class Solution:

    def numIslands2(self, m: int, n: int, positions):
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        u = UnionFind(len(positions))
        seen = {}
        count = 0
        for i, (x, y) in enumerate(positions):
            if (x, y) in seen:
                yield count
                continue
            seen[(x, y)] = i
            s = 0
            for dx, dy in directions:
                if (x + dx, y + dy) in seen:
                    s += u.connect(i, seen[(x + dx, y + dy)])
            if not s:
                count += 1
            else:
                count -= s - 1
            yield count
