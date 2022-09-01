from typing import List


class UnionFind:
    def __init__(self, size):
        self.array = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, x):
        if self.array[x] == x:
            return x
        self.array[x] = self.find(self.array[x])
        return self.array[x]

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi != yi:
            if self.rank[xi] > self.rank[yi]:
                self.array[yi] = xi
            elif self.rank[xi] < self.rank[yi]:
                self.array[xi] = yi
            else:
                self.array[xi] = yi
                self.rank[yi] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        u = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    u.union(i + 1, j + 1)
        result = 0
        for i, parent in enumerate(u.array[1:]):
            if i + 1 == parent:
                result += 1
        return result
