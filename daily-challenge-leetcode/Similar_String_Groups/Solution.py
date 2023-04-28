from typing import List


class UnionFind:

    def __init__(self, size):
        self.nodes = list(range(size))
        self.rank = [0] * size

    def union(self, x, y):
        if (xi := self.find(x)) == (yi := self.find(y)):
            return
        elif self.rank[xi] > self.rank[yi]:
            self.nodes[yi] = xi
        elif self.rank[xi] < self.rank[yi]:
            self.nodes[xi] = yi
        else:
            self.nodes[xi] = yi
            self.rank[yi] += 1

    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]


class Solution:

    def numSimilarGroups(self, S: List[str]) -> int:

        def similar(s, ss):
            diff = 0
            for _, (c, cc) in enumerate(zip(s, ss)):
                if c != cc:
                    diff += 1
                if diff > 2:
                    break
            else:
                return True
            return 

        strs = list(set(S))
        uf = UnionFind(n := len(strs))
        for i, s in enumerate(sorted(strs)):
            for j, ss in enumerate(sorted(strs)):
                if not similar(s, ss):
                    continue
                uf.union(i, j)
        return len(set(uf.find(i) for i in range(n)))