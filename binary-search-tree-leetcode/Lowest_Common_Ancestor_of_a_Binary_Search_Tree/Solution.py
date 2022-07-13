# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestorRec(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if p.val > q.val:
            p, q = q, p
        result = None

        def find(r):
            nonlocal result
            if not r:
                return
            if r.val >= p.val and r.val <= q.val:
                result = r
                return
            if not result:
                find(r.left)
            if not result:
                find(r.right)

        find(root)
        return result

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        current = root
        while current:
            if q.val > current.val and p.val > current.val:
                current = current.right
            elif q.val < current.val and p.val < current.val:
                current = current.left
            else:
                return current 