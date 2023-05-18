class Solution:

    def findSmallestSetOfVertices(self, n: int, edges):
        return {t[0] for t in edges} - {t[1] for t in edges}
