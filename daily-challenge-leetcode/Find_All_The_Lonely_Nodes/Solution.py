from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def find(root):
            if root.left and root.right:
                find(root.left)
                find(root.right)

            elif root.left:
                ans.append(root.left.val)
                find(root.left)

            elif root.right:
                ans.append(root.right.val)
                find(root.right)

        find(root)
        return ans
