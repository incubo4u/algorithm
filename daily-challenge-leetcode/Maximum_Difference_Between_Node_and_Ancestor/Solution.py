from typing import Optional
# Definition for a binary tree node.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def find_diff(root, lo, hi):
            if not root:
                return hi - lo

            lo, hi = min(root.val, lo), max(root.val, hi)
            return max(find_diff(root.left, lo, hi),
                       find_diff(root.right, lo, hi))

        return find_diff(root, root.val, root.val)
