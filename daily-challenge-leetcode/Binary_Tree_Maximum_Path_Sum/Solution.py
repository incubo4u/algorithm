from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def traverse(root):
            if not root:
                return 0
            l, r = max(traverse(root.left), 0), max(traverse(root.right), 0)
            nonlocal best
            best = max(best, l + r + root.val)
            return max(l + root.val, r + root.val)

        traverse(root)
        return best