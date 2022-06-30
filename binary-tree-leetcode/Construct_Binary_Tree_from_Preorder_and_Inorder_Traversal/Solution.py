# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 
        root = TreeNode(preorder[0])
        rootPostion = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:rootPostion+1],inorder[:rootPostion])
        root.right = self.buildTree(preorder[rootPostion+1:],inorder[rootPostion+1:])
        return root


