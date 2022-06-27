# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)

        if not root:
            return result
        traverse(root)
        return result
