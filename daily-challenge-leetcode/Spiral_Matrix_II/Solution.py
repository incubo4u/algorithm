class Solution:

    def generateMatrix(self, n: int):
        m = [[0] * n for _ in range(n)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        i = j = d = 0
        nr = 1
        s = 3
        while n:
            for c in range(n):
                m[i][j] = nr
                if c != n - 1:
                    nr += 1
                    i += directions[d][0]
                    j += directions[d][1]
            d = (d + 1) % 4
            s -= 1
            if not s:
                n -= 1
                s = 2
        return m