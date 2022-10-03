from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for _, (u, v, w) in enumerate(times):
            graph[u].append((w, v))
        seen = set()
        hp = [(0, k)]
        while hp:
            delay, node = heappop(hp)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n:
                return delay
            for _, (ngb_delay, ngb) in enumerate(graph[node]):
                heappush(hp, (ngb_delay + delay, ngb))
        return -1
