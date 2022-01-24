#!/usr/bin/env python
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        def invertNodes(root: Optional[TreeNode]) -> None:
            if root is not None:
                temp = root.left
                root.left = root.right
                root.right = temp
                invertNodes(root.left)
                invertNodes(root.right)
            else:
                return
        invertNodes(root)        
        return root