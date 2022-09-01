from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def traverse(root, match, pathLenght):
            nonlocal longest
            if not root:
                return

            if match == root.val:
                pathLenght += 1
                match += 1
            else:
                pathLenght = 1
                match = root.val + 1

            longest = max(pathLenght, longest)
            traverse(root.left, match, pathLenght)
            traverse(root.right, match, pathLenght)

        traverse(root, root.val, 0)
        return longest
