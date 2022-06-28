# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSym(rootOne, rootTwo):
            if not rootOne and not rootTwo:
                return True
            if not rootOne or not rootTwo:
                return False
            if rootOne.val == rootTwo.val:
                return checkSym(rootOne.left, rootTwo.right) and checkSym(rootOne.right, rootTwo.left)
            return False

        return checkSym(root, root)
