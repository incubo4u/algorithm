from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        h, w = len(mat), len(mat[0])
        y, x = 0, 0
        y_dir, x_dir = -1, +1

        def changeDirection():
            nonlocal y_dir, x_dir
            y_dir, x_dir = x_dir, y_dir

        for _ in range(h * w):
            ans.append(mat[y][x])
            if y + y_dir < 0 or x + x_dir > w - 1:
                changeDirection()
                if x < w - 1:
                    x += 1
                else:
                    y += 1

            elif y + y_dir > h - 1 or x + x_dir < 0:
                changeDirection()
                if y < h - 1:
                    y += 1
                else:
                    x += 1
            else:
                x += x_dir
                y += y_dir

        return ans
