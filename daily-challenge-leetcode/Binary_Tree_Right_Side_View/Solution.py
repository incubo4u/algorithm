# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = 0
        h = {}

        def view(root, d):
            if not root:
                return
            if d not in h:
                h[d] = root.val
            view(root.right, d + 1)
            view(root.left, d + 1)

        view(root, 0)
        return list(h.values())
