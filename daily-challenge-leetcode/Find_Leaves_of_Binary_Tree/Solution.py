from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root):
            if not root:
                return
            left = traverse(root.left)
            right = traverse(root.right)
            if left is None and right is None:
                leaf.append(root.val)
                return True
            if left:
                root.left = None
            if right:
                root.right = None
            return False

        ret = []
        while root.left or root.right:
            leaf = []
            traverse(root)
            ret.append(leaf)
        ret.append([root.val])
        return ret
