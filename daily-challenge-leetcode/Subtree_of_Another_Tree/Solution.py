# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif (not root and subRoot) or not subRoot:
            return False
        elif root.val != subRoot.val:
            return False
        return self.check(root.left, subRoot.left) and self.check(
            root.right, subRoot.right
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return
        elif root.val == subRoot.val and self.check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
