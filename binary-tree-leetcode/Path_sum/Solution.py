from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(root, score):
            if not root:
                return False
            score += root.val
            if score == targetSum and not root.left and not root.right:
                return True
            return search(root.left, score) or search(root.right, score)

        return search(root, 0)
