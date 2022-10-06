from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        g = defaultdict(list)
        for _, (start, destination, cost) in enumerate(flights):
            g[start].append((cost, destination))

        min_steps = [inf] * n
        min_cost = [inf] * n
        min_steps[src] = 0
        min_cost[src] = 0

        hq = [(0, 0, src)]
        while hq:
            cost, step, node = heappop(hq)
            if node == dst:
                return cost
            if step == k + 1:
                continue
            for _, (ngb_cost, ngb) in enumerate(g[node]):
                if ngb_cost + cost < min_cost[ngb]:
                    min_cost[ngb] = ngb_cost + cost
                    heappush(hq, (ngb_cost + cost, step + 1, ngb))
                    min_steps[ngb] = step
                elif step < min_steps[ngb]:
                    heappush(hq, (ngb_cost + cost, step + 1, ngb))

        return min_cost[dst] if min_cost[dst] < inf else -1
