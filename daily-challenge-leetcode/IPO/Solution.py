from heapq import heappop, heappush
from typing import List


class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:

        projects = list(zip(capital, profits))
        projects.sort()
        i = 0
        hq = []
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heappush(hq, -projects[i][1])
                i += 1
            if hq:
                w += -heappop(hq)
            else:
                break
        return w
