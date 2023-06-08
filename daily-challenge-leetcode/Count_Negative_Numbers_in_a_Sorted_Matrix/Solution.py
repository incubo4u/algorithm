from bisect import bisect_right


class Solution:

    def countNegatives(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        return sum(n - bisect_right(row, 0, key=lambda x: -x) for row in grid)
