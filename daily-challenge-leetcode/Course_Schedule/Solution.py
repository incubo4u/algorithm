from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for _, (source, dest) in enumerate(prerequisites):
            graph[source].append(dest)

        cache = {}

        def dfs(source, path):
            if source in cache:
                return cache[source]

            if source in path:
                cache[source] = False
                return False
            path.add(source)

            for next in graph[source]:
                if not dfs(next, path.copy()):
                    cache[source] = False
                    return False
            cache[source] = True
            return True

        for i in range(N):
            if not dfs(i, set()):
                return False
        return True
