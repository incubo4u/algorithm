class Solution:

    def findSmallestSetOfVertices(self, n: int, edges):
        u = {i: 0 for i in range(n)}
        for _, v in edges:
            u[v] += 1
        return [i for i in range(n) if not u[i]]
