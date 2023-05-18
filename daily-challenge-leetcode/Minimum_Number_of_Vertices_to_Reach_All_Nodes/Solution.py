class Solution:

    def findSmallestSetOfVertices(self, n: int, edges):
        return set((t[0] for t in edges)) - set((t[1] for t in edges))
