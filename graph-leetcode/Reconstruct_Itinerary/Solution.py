from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for _, (f, t) in enumerate(tickets):
            graph[f].append(t)
        path = ["JFK"]

        def travel(f):
            if len(path) > len(tickets):
                return True
            if f not in graph:
                return False

            temp = graph[f][::]
            for i, t in enumerate(temp):
                graph[f].pop(i)
                path.append(t)
                if travel(t):
                    return True
                graph[f].insert(i, t)
                path.pop()

        travel("JFK")
        return path
