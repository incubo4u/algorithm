from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        override = image[sr][sc]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        seen = set()
        m, n = len(image), len(image[0])

        def dfs(i, j):
            if i > m - 1 or j > n - 1 or 0 > j or 0 > i:
                return
            if (i, j) in seen or image[i][j] != override:
                return

            seen.add((i, j))
            image[i][j] = newColor
            for y, x in directions:
                dfs(i + y, j + x)

        dfs(sr, sc)
        return image
