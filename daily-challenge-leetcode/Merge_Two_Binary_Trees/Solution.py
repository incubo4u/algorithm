# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1=None, root2=None):
        if not root1 and not root2:
            return
        elif not root1:
            return TreeNode(
                root2.val, self.mergeTrees(root2.left), self.mergeTrees(root2.right)
            )
        elif not root2:
            return TreeNode(
                root1.val, self.mergeTrees(root1.left), self.mergeTrees(root1.right)
            )
        else:
            return TreeNode(
                root1.val + root2.val,
                self.mergeTrees(root1.left, root2.left),
                self.mergeTrees(root1.right, root2.right),
            )
