from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ret = []

        def dfs(n, path):
            if n == target:
                ret.append(path)
            for g in graph[n]:
                dfs(g, path + [g])
        dfs(0, [0])
        return ret
