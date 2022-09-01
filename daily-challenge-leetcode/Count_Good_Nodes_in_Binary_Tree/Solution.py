# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, limit):
            nonlocal count
            if not root:
                return
            if root.val >= limit:
                count += 1
            traverse(root.left, max(limit, root.val))
            traverse(root.right, max(limit, root.val))

        count = 0
        traverse(root, -float("inf"))
        return count
