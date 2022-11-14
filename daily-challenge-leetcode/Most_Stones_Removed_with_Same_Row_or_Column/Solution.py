from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, size):
        self.nodes = [i for i in range(size + 1)]
        self.rank = [0] * size

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
                self.nodes[yi] = xi
                self.rank[xi] += 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        u = UnionFind(len(stones))
        asix_x, asix_y = defaultdict(list), defaultdict(list)

        for i, (x, y) in enumerate(stones):
            asix_x[x].append(i)
            asix_y[y].append(i)

        for common in asix_x.values():
            for i in range(1, len(common)):
                u.union(common[i], common[i - 1])

        for common in asix_y.values():
            for i in range(1, len(common)):
                u.union(common[i], common[i - 1])
        ans = 0
        for i, root in enumerate(u.nodes):
            if i != root:
                ans += 1

        return ans
