from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def traverse(root, direction, dist):
            if not root:
                return
            nonlocal ans
            ans = max(ans, dist)
            if direction:
                traverse(root.left, not direction, dist + 1)
                traverse(root.left, direction, 0)
            else:
                traverse(root.right, not direction, dist + 1)
                traverse(root.right, direction, 0)

        traverse(root, True, 0)
        traverse(root, False, 0)
        return ans
