from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        def addOne(depth, root):
            if not root:
                return
            if depth == 2:
                root.left = TreeNode(val, left=root.left)
                root.right = TreeNode(val, right=root.right)
                return
            addOne(depth - 1, root.left)
            addOne(depth - 1, root.right)

        if depth == 1:
            return TreeNode(val, left=root)
        addOne(depth, root)
        return root
