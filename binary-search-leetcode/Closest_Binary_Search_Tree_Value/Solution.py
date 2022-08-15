# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    #     best = None
    #     bestDistance = float("infinity")

    #     def traverse(root):
    #         nonlocal best, bestDistance
    #         if not root or bestDistance == 0:
    #             return
    #         distance = abs(root.val - target)
    #         if bestDistance > distance:
    #             best = root.val
    #             bestDistance = distance
    #         if target > root.val:
    #             traverse(root.right)
    #         else:
    #             traverse(root.left)

    #     traverse(root)
    #     return best
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best = root.val
        while root:
            best = min(best, root.val, key=lambda val: abs(target - val))
            root = root.left if target < root.val else root.right
        return best
