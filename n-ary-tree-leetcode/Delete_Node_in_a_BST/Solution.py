# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:
            if not root.left and not root.right:
                return
            if not root.left and root.right:
                return root.right
            if not root.right and root.left:
                return root.left
            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.deleteNode(root.right, root.val)
            node = self.deleteNode(node, root.val)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
