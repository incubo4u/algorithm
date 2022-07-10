from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.iterator = 0
        self.exist = root is not None

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            self.inorder.append(root.val)
            traverse(root.right)

        traverse(root)

    def next(self) -> int:
        if self.iterator + 1 > len(self.inorder) - 1:
            self.exist = False
        self.iterator += 1
        return self.inorder[self.iterator - 1]

    def hasNext(self) -> bool:
        return self.exist


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
