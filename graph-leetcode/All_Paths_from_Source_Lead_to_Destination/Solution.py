from typing import List
from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for _, (a,b) in enumerate(edges):
            graph[a].append(b)
        colors = [0]*n
        def dfs(n):
            if colors[n] != 0:
                return colors[n] == 2
            colors[n] = 1
            if not graph[n]:
                return n == destination
            for _, node in enumerate(graph[n]):
                if not dfs(node):
                    return False
                colors[node] = 2
            return True
                
        return dfs(source)