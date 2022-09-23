from heapq import heappush, heappop
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

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        union_find = UnionFind(n)
        edges = []
        for i, (x, y) in enumerate(points):
            for j, (xx, yy) in enumerate(points):
                if i == j:
                    continue
                heappush(edges, (abs(x - xx) + abs(y - yy), i, j))
        cost = 0
        for _ in range(len(edges)):
            w, a, b = heappop(edges)
            if n == 1:
                break
            if union_find.connected(a, b):
                continue
            else:
                union_find.union(a, b)
                cost += w
                n -= 1
        return cost
