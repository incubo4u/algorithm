from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])
        gap = False
        while que:
            node = que.popleft()
            if not node:
                gap = True
                continue
            elif gap:
                return False
            que.append(node.left)
            que.append(node.right)
        return True
