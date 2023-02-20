from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode],
                        target: int) -> Optional[TreeNode]:

        def rm(root):
            if not root:
                return

            if rm(root.left):
                root.left = None

            if rm(root.right):
                root.right = None

            if not root.left and not root.right:
                return root.val == target

        rm(root)
        return root if root.val != target or root.left or root.right else None
