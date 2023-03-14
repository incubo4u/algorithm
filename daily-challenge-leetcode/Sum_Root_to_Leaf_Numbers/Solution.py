from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def traverse(root):
            if not root.left and not root.right:
                return [[root.val]]
            paths = []
            if root.left:
                paths += traverse(root.left)
            if root.right:
                paths += traverse(root.right)
            for nodes in paths:
                nodes.append(root.val)
            return paths

        ans = 0
        for path in traverse(root):
            n = 0
            for i, d in enumerate(path):
                n += d * (10**i)
            ans += n
        return ans

