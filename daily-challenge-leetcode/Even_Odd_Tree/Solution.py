# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([(root)])
        lvl = -1
        while que:
            l = len(que)
            lvl += 1
            odd_lvl, l_odd = lvl % 2, l % 2
            last = inf * odd_lvl
            for _ in range(l):
                curr = que.popleft()
                if odd_lvl and last <= curr.val:
                    return
                if not odd_lvl and last >= curr.val:
                    return
                if odd_lvl == curr.val % 2:
                    return
                last = curr.val
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
        return True
