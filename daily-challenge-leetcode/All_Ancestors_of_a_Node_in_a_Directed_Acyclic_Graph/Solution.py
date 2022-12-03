from collections import defaultdict, deque
from typing import List


class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]):
        indegree = defaultdict(int)
        g = defaultdict(set)

        for _, (f, t) in enumerate(edges):
            indegree[t] += 1
            g[f].add(t)

        ans = [set() for i in range(n)]
        que = deque(set(range(n)) - indegree.keys())
        while que:
            u = que.popleft()
            for v in g[u]:
                ans[v].add(u)
                ans[v] |= ans[u]
                indegree[v] -= 1
                if not indegree[v]:
                    que.append(v)

        return map(lambda a: sorted(a), ans)
