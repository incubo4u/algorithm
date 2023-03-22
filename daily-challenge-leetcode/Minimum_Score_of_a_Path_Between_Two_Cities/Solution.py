from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = inf
        g = defaultdict(list)
        for u,v,w in roads:
            g[u].append((w,v))
            g[v].append((w,u))
        
        seen = set()
        def dfs(node,w):
            nonlocal ans 
            ans = min(ans,w)
            if node in seen:
                return 
            seen.add(node)
            for distance, city in g[node]:
                if city != node:
                    dfs(city,distance)
        dfs(1,inf)
        return ans 