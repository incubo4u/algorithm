from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []
        index = -1

        def traverse(root):
            nonlocal index
            if not root:
                return
            traverse(root.left)
            inorder.append(root)
            if root == p:
                index = len(inorder)
            traverse(root.right)

        traverse(root)
        if inorder[-1] == p:
            return None
        return inorder[index]
