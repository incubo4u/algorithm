# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result = 0
        def depth(root,d):
            nonlocal result
            result = max(result,d)
            for node in root.children:
                depth(node,d+1)
        if not root:
            return 0
        depth(root,1)
        return result