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
        if xi != yi:
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
    def equationsPossible(self, equations: List[str]) -> bool:
        eq = UnionFind(26)
        diff = []
        for _, equation in enumerate(equations):
            x, op, y = ord(equation[:1]) - 97, equation[1:3], ord(equation[3:]) - 97
            if op == "!=":
                diff.append((x, y))
            else:
                eq.union(x, y)
        for _, (x, y) in enumerate(diff):
            if eq.connected(x, y):
                return False
        return True
