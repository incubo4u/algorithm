from collections import deque
from typing import List


class Solution:

    def isBipartite(self, g: List[List[int]]) -> bool:
        seen = {}

        def bfs(start):
            que = deque([start])
            seen[start] = 1
            while que:
                node = que.popleft()
                for n in g[node]:
                    if n in seen:
                        if seen[node] == seen[n]:
                            return
                        continue
                    seen[n] = -seen[node]
                    que.append(n)
            return True

        return all(bfs(i) for i in range(len(g)) if i not in seen)
