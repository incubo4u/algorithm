from ast import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:

    def longestPath(self, p: List[int], s: str) -> int:
        g = defaultdict(list)
        N = len(s)
        for node, parent in enumerate(p):
            if s[parent] == s[node] or parent == -1:
                continue
            g[parent].append(node)
            g[node].append(parent)
        seen = set()

        def traverse(root, prev):
            seen.add(root)
            hq = []
            for node in g[root]:
                if node == prev:
                    continue
                heappush(hq, traverse(node, root))
                if len(hq) >= 3:
                    heappop(hq)
            nonlocal best
            best = max(best, sum(hq) + 1)
            return max(hq, default=0) + 1

        best = 0
        for i in range(N):
            if i in seen:
                continue
            traverse(i, -1)
        return best
