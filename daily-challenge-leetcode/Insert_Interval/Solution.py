from bisect import bisect_left
from typing import List


class Solution:

    def insert(self, IT: List[List[int]], NIT: List[int]) -> List[List[int]]:
        IT.insert(bisect_left([s for s, _ in IT], NIT[0]), NIT)
        i = 0
        while i < len(IT):
            while i + 1 < len(IT) and IT[i][1] >= IT[i + 1][0]:
                s, e = IT.pop(i + 1)
                IT[i][0] = min(IT[i][0], s)
                IT[i][1] = max(IT[i][1], e)
            i += 1
        return IT
