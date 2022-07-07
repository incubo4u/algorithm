# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def find(r):
            nonlocal result
            if not r:
                return 0
            left = find(r.left)
            right = find(r.right)
            
            if left + right + int(r in (p, q)) == 2:
                result = r
            
            if r in (p,q):
                return 1
            return max(left, right)
        find(root)
        return result