# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        parents = {}
        que = deque([root])
        ans = root

        def remove(root):
            p = parents[root.val]
            if p.left == root:
                p.left = None
            if p.right == root:
                p.right = None

        while que:
            que_len = len(que)
            for _ in range(que_len):
                root = que.popleft()

                if root.left:
                    if root.left.val in parents:
                        remove(root)
                        return ans
                    parents[root.left.val] = root
                    que.append(root.left)

                if root.right:
                    if root.right.val in parents:
                        remove(root)
                        return ans
                    parents[root.right.val] = root
                    que.append(root.right)
