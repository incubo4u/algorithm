from ast import List


class Solution:

    def longestCycle(self, edges: List[int]) -> int:
        ans = 0
        path = {}

        def visit(n, c):
            start = c
            while n not in path and n != -1:
                path[n] = (c, start)
                n = edges[n]
                c += 1
            if n != -1 and path[n][1] == start:
                return c - path[n][0]
            return -1

        for i, n in enumerate(edges):
            if n in path or n == -1:
                continue
            if ans > (len(edges) - 1) - i:
                break
            ans = max(visit(n, i), ans)

        return ans if ans else -1
