from sys import maxsize
from typing import List, Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, leftLimit = None, rightLimit = None):
            if root is None:
                return True
            if (leftLimit is None or leftLimit > root.val) and \
                (rightLimit is None or root.val > rightLimit):
                leftValid = validate(root.left, root.val, rightLimit)
                if not leftValid:
                    return False
                rightValid = validate(root.right, leftLimit, root.val)
                if not rightValid:
                    return False
            else:
                return False
            return leftValid and rightValid
        return validate(root)