from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        score = 0
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def visit(i, j):
            for _, d in enumerate(directions):
                x, y = i + d[0], j + d[1]

                if 0 > x or x > len(grid) - 1 or 0 > y or y > len(grid[0]) - 1:
                    continue

                elif grid[x][y] == "x" or grid[x][y] == "0":
                    continue

                else:
                    grid[x][y] = "x"
                    visit(x, y)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    score += 1
                    visit(i, j)
        return score
