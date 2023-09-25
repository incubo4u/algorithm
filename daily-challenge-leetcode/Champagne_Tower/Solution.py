class Solution:

    def champagneTower(self, poured: int, r: int, c: int) -> float:
        piramid = [[0] * k for k in range(1, r + 3)]
        piramid[0][0] = poured
        for i in range(r):
            for j in range(i + 1):
                overflow = (piramid[i][j] - 1) / 2
                if overflow > 0:
                    piramid[i + 1][j] += overflow
                    piramid[i + 1][j + 1] += overflow
        return min(1, piramid[r][c])
