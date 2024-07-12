# Runtime Percentile: 5.427499999999892
# Memory Percentile: 100.0


class UnionFind:

    def __init__(self, size):
        self.nodes = list(range(size + 1))
        self.rank = [0] * (size + 1)

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi: return

        if self.rank[xi] > self.rank[yi]:
            self.nodes[yi] = xi
        elif self.rank[xi] < self.rank[yi]:
            self.nodes[xi] = yi
        else:
            self.nodes[xi] = yi
            self.rank[yi] += 1
        return True

    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        bob_edges = set()
        alice_edges = set()
        ans = 0
        edges.sort(key=lambda l: -l[0])

        while edges:
            t, u, v = edges.pop(0)
            edge = (u, v)
            if t == 3:
                if b := bob.union(u, v):
                    bob_edges.add(edge)
                if a := alice.union(u, v):
                    alice_edges.add(edge)
                if not a or not b:
                    ans += 1
            elif t == 2:
                if bob.union(u, v):
                    bob_edges.add(edge)
                else:
                    ans += 1
            else:
                if alice.union(u, v):
                    alice_edges.add(edge)
                else:
                    ans += 1

        return ans if len(alice_edges) == n - 1 == len(bob_edges) else -1
