class Solution:

    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        M = P = G = 0
        for i, g in enumerate(garbage):
            if 'M' in g: M = i
            if 'P' in g: P = i
            if 'G' in g: G = i
        n = len(garbage)
        cost = 0
        for i in range(n):
            if i < M: cost += travel[i]
            if i < P: cost += travel[i]
            if i < G: cost += travel[i]
            cost += len(garbage[i])
        return cost
