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
            if self.nodes[xi] > self.nodes[yi]:
                self.nodes[yi] = xi
            elif self.nodes[xi] < self.nodes[yi]:
                self.nodes[xi] = yi
            else:
                self.nodes[xi] = yi
                self.rank[yi] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = UnionFind(n)
        for _, (x, y) in enumerate(edges):
            u.union(x, y)
        return len(set(map(u.find, u.nodes)))
