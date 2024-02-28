# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        while que:
            l = len(que)
            for _ in range(l):
                curr = que.popleft()
                if curr.right:
                    que.append(curr.right)
                if curr.left:
                    que.append(curr.left)
        return curr.val
