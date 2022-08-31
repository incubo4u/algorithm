from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()
        result = []

        def dfs(y, x, seen, bound=-float("inf")):
            if (
                (y, x) in seen
                or x > n - 1
                or y > m - 1
                or x < 0
                or y < 0
                or heights[y][x] < bound
            ):
                return
            seen.add((y, x))
            for d in directions:
                dfs(y + d[1], x + d[0], seen, heights[y][x])

        for y in range(m):
            dfs(y, 0, pacific)
            dfs(y, n - 1, atlantic)
        for x in range(n):
            dfs(0, x, pacific)
            dfs(m - 1, x, atlantic)

        return pacific & atlantic
