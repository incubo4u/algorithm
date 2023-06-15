from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        INF = 1000000
        lvl = best_lvl = s = 0
        best_s = -INF
        que = deque([root])
        while que:
            floor_lenght = len(que)
            s = 0
            lvl += 1
            for _ in range(floor_lenght):
                root = que.popleft()
                s += root.val
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
            if s > best_s:
                best_s = s
                best_lvl = lvl

        return best_lvl
