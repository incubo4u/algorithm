# Runtime Percentile: 89.6415
# Memory Percentile: 15.537900000000008


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def splitBST(self, root: Optional[TreeNode],
                 target: int) -> List[Optional[TreeNode]]:
        if not root:
            return None, None

        if root.val <= target:
            root.right, main_tree_node = self.splitBST(root.right, target)
            return root, main_tree_node

        other_tree_node, root.left = self.splitBST(root.left, target)
        return other_tree_node, root
