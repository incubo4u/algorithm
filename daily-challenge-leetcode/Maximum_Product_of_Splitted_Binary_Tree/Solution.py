from typing import Optional
# Definition for a binary tree node.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = (10**9) + 7

        def total(root):
            if not root:
                return 0
            return root.val + total(root.left) + total(root.right)

        def max_prod(root):
            if not root:
                return 0
            curr = root.val + max_prod(root.left) + max_prod(root.right)
            nonlocal prod
            prod = max((s - curr) * curr, prod)
            return curr

        s = total(root)
        prod = 0
        max_prod(root)
        return prod % MOD