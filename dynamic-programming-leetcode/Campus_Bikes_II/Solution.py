from functools import cache


class Solution:

    def assignBikes(self, workers, bikes) -> int:
        W, B = len(workers), len(bikes)

        def distance(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        @cache
        def get_min(w, seen):
            if w > W - 1:
                return 0
            best = 10000
            for b in range(B):
                if seen & (1 << b):
                    continue
                best = min(
                    get_min(w + 1, seen | (1 << b)) + distance(w, b), best)
            return best

        return get_min(0, 0)
