from collections import Counter, defaultdict
from typing import List


class UnionFind:

    def __init__(self, size):
        self.nodes = list(range(size))
        self.rank = [0] * size

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi:
            return
        elif self.rank[xi] > self.rank[yi]:
            self.nodes[yi] = xi
        elif self.rank[xi] < self.rank[yi]:
            self.nodes[xi] = yi
        else:
            self.nodes[yi] = xi
            self.rank[xi] += 1

    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]


class Solution:

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        size = len(vals)
        ans = 0
        val_idx = defaultdict(list)
        tree = defaultdict(list)

        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        for i, val in enumerate(vals):
            val_idx[val].append(i)

        uf = UnionFind(size)
        c = Counter()
        for _, (val, idxs) in enumerate(sorted(val_idx.items())):
            for i in idxs:
                for ngb in tree[i]:
                    if val >= vals[ngb]:
                        uf.union(i, ngb)
            for i in idxs:
                root = uf.find(i)
                c[root] += 1
                ans += c[root]
            c.clear()
        return ans
