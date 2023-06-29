from collections import defaultdict
from heapq import heappop, heappush


class Solution:

    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(list)
        max_prob = defaultdict(float)
        seen = set()
        n = len(edges)
        for i in range(n):
            (u, v) = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        max_prob[start] = 1
        hq = [(-1, start)]
        while hq:
            path_p, u = heappop(hq)
            if u in seen:
                continue
            seen.add(u)
            if u == end:
                return -path_p
            for v, prob in graph[u]:
                if (best_p := -path_p * prob) > max_prob[v]:
                    max_prob[v] = best_p
                    heappush(hq, (-best_p, v))
        return 0
