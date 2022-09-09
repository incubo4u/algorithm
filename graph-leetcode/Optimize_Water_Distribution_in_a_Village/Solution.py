from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:

        edgestuple = []
        N = n + len(wells) + 1
        allEdges = N - 1
        visited = [False] * N
        adjacency = [set() for i in range(N)]

        for i, cost in enumerate(wells):
            if i + 1 > 1:
                edgestuple.append((0, n + i, n + 1 + i))
            edgestuple.append((cost, i + 1, n + 1 + i))

        for _, (start, end, cost) in enumerate(pipes):
            edgestuple.append((cost, start, end))

        for _, (cost, start, end) in enumerate(edgestuple):
            adjacency[start].add((cost, start, end))
            adjacency[end].add((cost, end, start))

        minheap = []
        edgeCount, result = 0, 0

        def addEdge(n):
            visited[n] = True
            for pipe in adjacency[n]:
                if not visited[pipe[2]]:
                    heappush(minheap, pipe)

        addEdge(1)
        while minheap and edgeCount != allEdges:
            edge = heappop(minheap)
            nextNode = edge[2]
            if visited[nextNode]:
                continue
            edgeCount += 1
            result += edge[0]
            addEdge(nextNode)

        for i, seen in enumerate(visited[1:]):
            if not seen:
                result += wells[i]

        return result
