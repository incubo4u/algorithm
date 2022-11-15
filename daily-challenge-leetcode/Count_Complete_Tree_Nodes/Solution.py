from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def rightHeight(root):
            h = 0
            while root:
                h += 1
                root = root.right
            return h

        def leftHeight(root):
            h = 0
            while root:
                h += 1
                root = root.left
            return h

        left, right = leftHeight(root), rightHeight(root)
        if left > right:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        else:
            return (2**left) - 1
