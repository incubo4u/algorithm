from collections import defaultdict, deque
from math import inf


class Solution:

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]],
                                 blueEdges: List[List[int]]) -> List[int]:

        blue = defaultdict(list)
        red = defaultdict(list)

        for a, b in blueEdges:
            blue[a].append(b)

        for u, v in redEdges:
            red[u].append(v)

        que = deque([(True, 0, 0), (False, 0, 0)])
        ans = [inf] * n
        while que:
            color, node, distance = que.popleft()
            ans[node] = min(ans[node], distance)
            if color:
                que.extend(((False, u, distance + 1) for u in blue[node]))
                del blue[node]
            else:
                que.extend(((True, u, distance + 1) for u in red[node]))
                del red[node]
        return map(lambda i: -1 if i == inf else i, ans)
