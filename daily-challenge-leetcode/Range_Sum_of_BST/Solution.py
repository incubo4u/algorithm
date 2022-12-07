from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0

        def get_range_sum(node):
            if not node:
                return
            if low <= node.val <= high:
                nonlocal s
                s += node.val
            if node.val > low:
                get_range_sum(node.left)
            if node.val < high:
                get_range_sum(node.right)

        get_range_sum(root)
        return s
