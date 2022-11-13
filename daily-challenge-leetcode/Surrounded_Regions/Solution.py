from typing import List


class Solution:
    def solve(self, mat: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def dfs(i, j):

            if i > len(mat) - 1 or i < 0 or j > len(mat[0]) - 1 or j < 0:
                return
            if (i, j) in seen or mat[i][j] == "X":
                return
            seen.add((i, j))

            for di, dj in directions:
                dfs(i + di, j + dj)

        for j in range(len(mat[0])):
            dfs(0, j)
            dfs(len(mat) - 1, j)
        for i in range(len(mat)):
            dfs(i, 0)
            dfs(i, len(mat[0]) - 1)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == "O" and (i, j) not in seen:
                    mat[i][j] = "X"
