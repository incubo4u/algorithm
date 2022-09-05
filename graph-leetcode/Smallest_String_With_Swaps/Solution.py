from collections import defaultdict
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


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        lenght = len(s)
        u = UnionFind(lenght)
        for _, (i, j) in enumerate(pairs):
            u.union(i, j)

        graphs = defaultdict(list)
        for i in range(lenght):
            root = u.find(i)
            graphs[root].append(i)

        ret = list(s)
        for indexes in graphs.values():
            chars = [s[i] for i in indexes]
            chars.sort()
            for i, pos in enumerate(indexes):
                ret[pos] = chars[i]
        return "".join(ret)
