from collections import deque
from typing import List


class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int,node2: int) -> int:

        def bfs(node):
            que = deque([(0, node)])
            seen = {}
            while que:
                d, n = que.popleft()
                if n in seen:
                    continue
                seen[n] = d
                if edges[n] != -1:
                    que.append((d + 1, edges[n]))
            return seen

        dist = ans = 100001
        one, two = bfs(node1), bfs(node2)
        for key in one:
            if key not in two:
                continue
            elif dist > (d := max(one[key], two[key])) or (dist == d and key < ans):
                ans = key
                dist = d
        return ans if ans < 100001 else -1