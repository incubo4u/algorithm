from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []

        def traverse(root, path):
            if not root:
                return
            if not root.left and not root.right and sum(path + [root.val]) == targetSum:
                ret.append(path + [root.val])
            traverse(root.left, path + [root.val])
            traverse(root.right, path + [root.val])

        traverse(root, [])
        return ret
