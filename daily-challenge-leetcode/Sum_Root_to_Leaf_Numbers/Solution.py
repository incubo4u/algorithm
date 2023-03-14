from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def traverse(root, curr):
            if not root:
                return
            curr *= 10
            curr += root.val
            if not (root.left or root.right):
                nonlocal ans
                ans += curr

            traverse(root.left, curr)
            traverse(root.right, curr)

        traverse(root, 0)
        return ans
