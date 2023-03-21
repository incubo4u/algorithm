# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:

    def copyRandomBinaryTree(self, root):
        seen = {}

        def deepCopy(root, h, left, right, random):
            if not root:
                return
            ret = False
            if (key := hash(root)) not in seen:
                seen[key] = NodeCopy(root.val)
            else:
                ret = True
            if left:
                seen[h].left = seen[key]
            if right:
                seen[h].right = seen[key]
            if random:
                seen[h].random = seen[key]
            if ret:
                return
            deepCopy(root.left, key, 1, 0, 0)
            deepCopy(root.right, key, 0, 1, 0)
            deepCopy(root.random, key, 0, 0, 1)

        deepCopy(root, hash(root), 0, 0, 0)
        return seen[key] if (key := hash(root)) in seen else None