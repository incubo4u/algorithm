# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]):
        if not root:
            return ()
        que = deque([root])
        ans = []
        while que:
            ans.append([])
            lenght = len(que)
            for _ in range(lenght):
                node = que.popleft()
                ans[-1].append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return (elm if i % 2 else elm[::-1] for i, elm in enumerate(ans, 1))
