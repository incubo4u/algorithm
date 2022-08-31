from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []

        def dfs(y, x, bound, seen):
            nonlocal atlantic, pacific
            if (
                y > len(heights) - 1
                or x > len(heights[y]) - 1
                or y < 0
                or x < 0
                or (y, x) in seen
                or bound < heights[y][x]
            ):
                return

            seen.add((y, x))
            if y == len(heights) - 1 or x == len(heights[y]) - 1:
                atlantic = True
            if y == 0 or x == 0:
                pacific = True

            for d in directions:
                if atlantic and pacific:
                    return
                dfs(y + d[1], x + d[0], heights[y][x], seen)

        for y in range(len(heights)):
            for x in range(len(heights[y])):
                atlantic, pacific = False, False
                dfs(y, x, float("inf"), set())
                if atlantic and pacific:
                    result.append((y, x))
        return result
