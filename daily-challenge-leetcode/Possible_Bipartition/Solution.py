from collections import defaultdict, deque
from typing import List


class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        tuple(
            map(lambda persons:
             g[persons[0]-1].append(persons[1]-1) or
             g[persons[1]-1].append(persons[0]-1),
             dislikes))
             
        grey, black, white = 0, 1, 2
        colors = [grey] * n
        que = deque()

        def paint(node):
            colors[node] = black
            que.append(node)
            while que:
                curr = que.popleft()
                for ngb in g[curr]:
                    if colors[ngb]:
                        continue
                    elif colors[curr] == black:
                        colors[ngb] = white
                    else:
                        colors[ngb] = black
                    que.append(ngb)

        tuple(
            map(lambda node:
                not colors[node]
                and paint(node)
                or que.clear(),
                range(n)))

        return not any(colors[a - 1] == colors[b - 1] for a, b in dislikes)
