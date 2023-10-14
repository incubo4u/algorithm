class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def paint(i, waiting):
            if waiting >= n:
                return 0
            if i > n - 1:
                return inf

            return min(
                paint(i + 1, waiting + time[i] + 1) + cost[i],
                paint(i + 1, waiting))

        return paint(0, 0)
