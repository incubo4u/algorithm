# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        ret = []
        q = []
        q.append(root)
        while len(q) > 0:
            floor = []
            qLen = len(q)
            for i in range(qLen):
                node = q.pop(0)
                if node:
                    floor.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(floor) > 0:
                ret.append(floor)
        return ret
