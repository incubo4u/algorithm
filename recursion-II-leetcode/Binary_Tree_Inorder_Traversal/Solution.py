# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        ret = []
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            ret.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return ret