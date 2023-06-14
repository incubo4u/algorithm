from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        INF = 1000000

        def dfs(root, l, r):
            if not root:
                return INF
            return min(
                abs(root.val - r),
                abs(root.val - l),
                dfs(root.left, l, root.val),
                dfs(root.right, root.val, r),
            )

        return dfs(root, INF, INF)
