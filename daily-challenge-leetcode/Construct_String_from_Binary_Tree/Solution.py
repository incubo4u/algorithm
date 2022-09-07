from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        tree = ""

        def traverse(root):
            nonlocal tree
            if not root:
                return
            tree += "("
            tree += str(root.val)
            if not root.left and root.right:
                tree += "()"
                traverse(root.right)
            else:
                traverse(root.left)
                traverse(root.right)
            tree += ")"

        traverse(root)
        return tree[1 : len(tree) - 1]
