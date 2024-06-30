# Runtime Percentile: 40.63750000000002
# Memory Percentile: 58.56580000000001


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def splitBST(self, root: Optional[TreeNode],
                 target: int) -> List[Optional[TreeNode]]:

        def split(root):
            if not root:
                return None, None

            if root.val <= target:
                root.right, main_tree_node = split(root.right)
                return root, main_tree_node

            other_tree_node, root.left = split(root.left)
            return other_tree_node, root

        return split(root)
