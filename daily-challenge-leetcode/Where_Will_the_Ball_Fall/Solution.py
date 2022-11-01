from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n

        def traverse(i, j, last_dir, ball_nr):
            if j > n - 1 or j < 0:
                return

            if i == m:
                return j

            curr = grid[i][j]
            left = grid[i][j - 1] if j - 1 >= 0 else None
            right = grid[i][j + 1] if j + 1 < n else None

            if curr == last_dir == right == 1:
                return traverse(i + 1, j + 1, curr, ball_nr)
            elif curr == last_dir == left == -1:
                return traverse(i + 1, j - 1, curr, ball_nr)
            elif curr != last_dir and curr == left == -1:
                return traverse(i + 1, j - 1, curr, ball_nr)
            elif curr != last_dir and curr == right == 1:
                return traverse(i + 1, j + 1, curr, ball_nr)

        for j in range(0, n):
            end_pos = traverse(0, j, grid[0][j], j)
            if end_pos is not None:
                ans[j] = end_pos
        return ans
