# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        def traverse(node):
            for n in node.children:
                traverse(n)
                ret.append(n.val)

        if not root:
            return
        ret = []
        traverse(root)
        ret.append(root.val)
        return ret
