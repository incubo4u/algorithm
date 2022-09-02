from typing import List


class UnionFind:
    def __init__(self, size):
        self.nodes = [i for i in range(size)]
        self.rank = [1] * (size)

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
            return True
        else:
            return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        u = UnionFind(n)
        for _, (x, y) in enumerate(edges):
            if not u.union(x, y):
                return False
        return True
