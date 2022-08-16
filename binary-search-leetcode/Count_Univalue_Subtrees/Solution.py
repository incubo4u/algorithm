from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        score = 0

        def traverse(root):
            nonlocal score
            if not root:
                return

            left = traverse(root.left)
            right = traverse(root.right)

            if left is None and right is None:
                score += 1
                return root
            elif left and right and left.val == right.val == root.val:
                score += 1
                return root
            elif left and right is None and left.val == root.val:
                score += 1
                return root
            elif right and left is None and right.val == root.val:
                score += 1
                return root
            else:
                return False

        traverse(root)
        return score
