from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            l = traverse(root.left)
            r = traverse(root.right)
            if not l:
                root.left = None
            if not r:
                root.right = None

            return root.val == 1 or l or r

        traverse(root)
        if not root.val and not root.left and not root.right:
            return
        return root
