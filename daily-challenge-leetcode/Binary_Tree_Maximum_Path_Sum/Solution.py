from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def traverse(root):
            if not root:
                return False
            l, r = traverse(root.left), traverse(root.right)
            nonlocal best
            best = max(best, root.val)
            if l and r:
                best = max(best, l + root.val, r + root.val, l + r + root.val)
                return max(l + root.val, r + root.val, root.val)
            elif l:
                best = max(best, l + root.val, l)
                return max(l + root.val, root.val)
            elif r:
                best = max(best, r + root.val, r)
                return max(r + root.val, root.val)
            return root.val

        traverse(root)
        return best
