# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def traverse(node):
            for n in node.children:
                ret.append(n.val)
                traverse(n)
        if not root:
            return
        ret = [root.val]        
        traverse(root)
        return ret
            