from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = {}

        def traverse(root, i=0, depth=0):
            if not root:
                return
            if i not in memo:
                memo[i] = [(root.val, depth)]
            else:
                memo[i].append((root.val, depth))
            traverse(root.left, i - 1, depth + 1)
            traverse(root.right, i + 1, depth + 1)

        traverse(root)
        return [
            [node[0] for node in sorted(memo[i], key=lambda node: node[1])]
            for i in sorted(memo.keys())
        ]
