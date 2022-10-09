from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        need = set()

        def search(root):
            if not root:
                return
            if root.val in need:
                return True
            need.add(k - root.val)
            return search(root.left) or search(root.right)

        return search(root)

    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     need = set()
    #     stack = [root]
    #     while stack:
    #         root = stack.pop()
    #         if not root:
    #             continue
    #         if k - root.val in need:
    #             return True
    #         need.add(root.val)
    #         stack.append(root.left)
    #         stack.append(root.right)
    #     return False
