from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        INF = 10**5
        dist = [[INF for i in range(n)] for j in range(m)]
        que = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    que.append((i, j))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while que:
            curr = que.popleft()
            for y, x in directions:
                next = (curr[0] + y, curr[1] + x)
                if next[0] < 0 or next[1] < 0 or next[0] > m - 1 or next[1] > n - 1:
                    continue
                if dist[next[0]][next[1]] > dist[curr[0]][curr[1]] + 1:
                    dist[next[0]][next[1]] = dist[curr[0]][curr[1]] + 1
                    que.append(next)
        return dist
