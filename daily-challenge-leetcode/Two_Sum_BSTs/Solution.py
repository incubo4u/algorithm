from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode],
                   target: int) -> bool:
        seen_one = set()
        que = deque([root1])
        while que:
            node = que.popleft()
            seen_one.add(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        que.append(root2)
        while que:
            node = que.popleft()
            if target - node.val in seen_one:
                return True
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return
