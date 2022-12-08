# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def leafSimilar(self, root1, root2) -> bool:

        def get_leaf(root):
            if not root:
                return
            elif not root.left and not root.right:
                leaf.append(root.val)
            else:
                get_leaf(root.left)
                get_leaf(root.right)

        leaf = []
        get_leaf(root1)
        tmp = leaf[::]
        leaf.clear()
        get_leaf(root2)
        return tmp == leaf
