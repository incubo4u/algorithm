from ast import List
from heapq import heappop, heappush


class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int,node2: int) -> int:

        def djikstra(node):
            hq = [(0, node)]
            seen = {}
            while hq:
                d, n = heappop(hq)
                if n in seen:
                    continue
                seen[n] = d
                if edges[n] != -1:
                    heappush(hq, (d + 1, edges[n]))
            return seen

        dist = ans = 100001
        one, two = djikstra(node1), djikstra(node2)
        for key in one:
            if key not in two:
                continue
            elif dist > (d := max(one[key], two[key])) or (dist == d
                                                           and key < ans):
                ans = key
                dist = d
        return ans if ans < 100001 else -1