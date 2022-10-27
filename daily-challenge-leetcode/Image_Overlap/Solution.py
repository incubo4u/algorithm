from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, F: List[List[int]], S: List[List[int]]) -> int:
        def get_ones(matrix):
            n = len(F)
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > 0:
                        yield (i, j)

        vectors = defaultdict(int)
        best_overlap = 0
        for _, (xf, yf) in enumerate(get_ones(F)):
            for _, (xs, ys) in enumerate(get_ones(S)):
                v = (xf - xs, yf - ys)
                vectors[v] += 1
                best_overlap = max(vectors[v], best_overlap)
        return best_overlap
