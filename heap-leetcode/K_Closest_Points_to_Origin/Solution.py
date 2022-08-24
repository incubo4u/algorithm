from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))[:k]
