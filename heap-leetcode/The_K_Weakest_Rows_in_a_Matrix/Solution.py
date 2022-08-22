import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            heapq.heappush(heap, (sum(row), i))
        return [smallest[1] for smallest in heapq.nsmallest(k, heap)]
        # mat = [(sum(row), index) for index, row in enumerate(mat)]
        # heapq.heapify(mat)
        # return [ smallest[1] for smallest in heapq.nsmallest(k, mat)]