from heapq import heappop, heappush
from itertools import product


class Solution:

    def assignBikes(self, workers: List[List[int]],
                    bikes: List[List[int]]) -> List[int]:
        hq = []
        n = len(workers)
        for (wi, (wx, wy)), (bi, (bx, by)) in product(enumerate(workers),
                                                      enumerate(bikes)):
            heappush(hq, (abs(wx - bx) + abs(wy - by), wi, bi))

        while n:
            _, wi, bi = heappop(hq)
            if type(workers[wi]) == type(bikes[bi]) == list:
                workers[wi] = bi
                bikes[bi] = wi
                n -= 1

        return workers
