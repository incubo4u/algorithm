from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        area = 0

        def maxArea(i, j, islandArea):
            for d in directions:
                x, y = i + d[0], j + d[1]
                if x not in range(len(grid)) or y not in range(len(grid[x])):
                    continue
                if grid[x][y] != -1 and grid[x][y] != 0:
                    islandArea += 1
                    grid[x][y] = -1
                    islandArea = maxArea(x, y, islandArea)
            return islandArea

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0 and grid[i][j] != -1:
                    grid[i][j] = -1
                    area = max(maxArea(i, j, 1), area)
        return area
