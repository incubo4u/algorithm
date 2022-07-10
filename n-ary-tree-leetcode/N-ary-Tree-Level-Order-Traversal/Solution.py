from typing import List
# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        ret = []
        que = [root]
        while len(que) > 0:
            floor = []
            lenght = len(que)
            for i in range(lenght):
                node = que.pop(0)
                floor.append(node.val)
                que.extend(node.children)
            if len(floor) > 0:
                ret.append(floor)
        return ret
        