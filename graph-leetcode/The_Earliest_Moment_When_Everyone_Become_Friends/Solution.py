from typing import List


class UnionFind:
    def __init__(self, size):
        self.nodes = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi != yi:
            if self.rank[xi] > self.rank[yi]:
                self.nodes[yi] = xi
            elif self.rank[xi] < self.rank[yi]:
                self.nodes[xi] = yi
            else:
                self.nodes[xi] = yi
                self.rank[yi] += 1
            return 1
        return 0


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if n-1 > len(logs): return -1
        u = UnionFind(n)
        logs.sort()
        for i, (time, a, b) in enumerate(logs):
            n -= u.union(a, b)
            if n == 1:
                return time
        return -1
