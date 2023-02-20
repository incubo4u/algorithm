from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findNearestRightNode(self, root: TreeNode,
                             u: TreeNode) -> Optional[TreeNode]:
        que = deque([root])
        while que:
            lenght = len(que)
            for i in range(lenght):
                node = que.popleft()
                if node == u:
                    return que.popleft() if i < lenght - 1 else None
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
