from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return [i for i in range(n)]

        g = defaultdict(list)
        indegree = defaultdict(int)
        for _, (u, v) in enumerate(edges):
            g[u].append(v)
            g[v].append(u)

        que = deque()
        for _, (node, ngbs) in enumerate(g.items()):
            indegree[node] = len(ngbs)
            if len(ngbs) < 2:
                que.append(node)
                indegree[node] -= 1

        ans = []
        while que:
            ans.clear()
            ql = len(que)
            for _ in range(ql):
                node = que.popleft()
                ans.append(node)
                for n in g[node]:
                    indegree[n] -= 1
                    if indegree[n] == 1:
                        que.append(n)
        return ans
