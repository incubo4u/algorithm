from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for key in words:
            d[key] += 1
        heap = [(-value, key) for _, (key, value) in enumerate(d.items())]
        heapify(heap)
        ret = []
        for _ in range(k):
            ret.append(heappop(heap)[1])
        return ret
