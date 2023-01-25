# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root, k):

        def traverse(root):
            nonlocal k
            if not root:
                return -1
            left = traverse(root.left)
            k -= 1
            if not k:
                return root.val
            right = traverse(root.right)
            return max(left, right)

        return traverse(root)
