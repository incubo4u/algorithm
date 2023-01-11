from collections import defaultdict
from typing import List


class Solution:

    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        g = defaultdict(list)
        for v, u in edges:
            g[v].append(u)
            g[u].append(v)

        def dfs(node, prev):
            total_time = 0
            for v in g[node]:
                if v == prev:
                    continue
                time = dfs(v, node)
                total_time += time + 2 if time or hasApple[v] else 0
            return total_time

        return dfs(0, 0)
