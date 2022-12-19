from typing import List


class UnionFind:

    def __init__(self, size):
        self.nodes = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi:
            return
        if self.rank[xi] > self.rank[yi]:
            self.nodes[yi] = xi
        elif self.rank[xi] < self.rank[yi]:
            self.nodes[xi] = yi
        else:
            self.nodes[xi] = yi
            self.rank[yi] += 1


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int,
                  destination: int) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.find(source) == uf.find(destination)
