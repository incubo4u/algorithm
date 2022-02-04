# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start,end):
            if start > end:
                return [None]
            trees = []
            for root in range(start,end+1):
                for left in generate(start,root-1):
                    for right in generate(root+1,end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees
        return generate(1,n)
s = Solution()
s.generateTrees(3)