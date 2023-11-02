# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def count(root):
            if not root:
                return 0, 0
            sum_right, count_right = count(root.right)
            sum_left, count_left = count(root.left)
            elm_count = count_left + count_right + 1
            sum_nodes = sum_right + sum_left + root.val
            nonlocal ans
            ans += int(sum_nodes // elm_count == root.val)
            return sum_nodes, elm_count

        count(root)
        return ans
