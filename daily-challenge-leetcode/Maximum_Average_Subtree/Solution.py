from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0

        def traverse(root):
            if not root:
                return 0, 0
            l, lcount = traverse(root.right)
            r, rcount = traverse(root.left)
            tree_sum = root.val + l + r
            node_count = lcount + rcount + 1
            nonlocal ans
            ans = max(ans, tree_sum / node_count)
            return tree_sum, node_count

        traverse(root)
        return ans
