from collections import deque
from itertools import chain
from typing import List

class Node:
    
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(set(chain.from_iterable(grid))) == 1:
            return Node(grid[0][0], 1, None, None, None, None)
        n = len(grid)
        root = Node(1, 0, None, None, None, None)
        mid = n // 2
        que = deque([((0, 0), mid, 'topLeft', root),
                     ((mid, 0), mid, 'topRight', root),
                     ((0, mid), mid, 'bottomLeft', root),
                     ((mid, mid), mid, 'bottomRight', root)])
        while que:
            (x, y), lenght, child, parent = que.popleft()
            elm = set(chain.from_iterable(map(lambda g: g[x:x + lenght],grid[y:y + lenght])))
            if lenght < 2 or len(elm) == 1:
                parent.__dict__[child] = Node(grid[y][x], 1, None, None,None, None)
            else:
                lenght //= 2
                parent.__dict__[child] = (node := Node(1, 0, None, None, None,None))
                que.append(((x, y), lenght, 'topLeft', node))
                que.append(((x + lenght, y), lenght, 'topRight', node))
                que.append(((x, y + lenght), lenght, 'bottomLeft', node))
                que.append(((x + lenght, y + lenght), lenght, 'bottomRight', node))
        return root
