# Runtime Percentile: 59.960200000000015
# Memory Percentile: 92.62950000000001


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def splitBST(self, root: Optional[TreeNode],
                 target: int) -> List[Optional[TreeNode]]:

        def find(root):
            if not root:
                return None, None
            if root.val <= target:
                root.right, ok = find(root.right)
                return root, ok
            else:
                discard, root.left = find(root.left)
                return discard, root

        return find(root)
