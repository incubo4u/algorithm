# Runtime Percentile: 85.34949999999998
# Memory Percentile: 69.35479999999998


class UnionFind:

    def __init__(self, size):
        self.rank = [0] * size
        self.nodes = list(range(size))

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi: return 0
        if self.rank[xi] > self.rank[yi]:
            self.nodes[xi] = yi
        elif self.rank[xi] < self.rank[yi]:
            self.nodes[yi] = xi
        else:
            self.nodes[yi] = xi
            self.rank[xi] += 1
        return 1

    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]


class Solution:

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()
        count = 0
        for t, x, y in logs:
            count += uf.union(x, y)
            if count == n - 1:
                return t
        return -1
