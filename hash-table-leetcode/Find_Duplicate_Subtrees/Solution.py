from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}

        def traverse(root):
            if not root:
                return hash("")

            leftHash = traverse(root.left)
            rightHash = traverse(root.right)
            currentHash = hash((leftHash, hash(str(root.val)), rightHash))

            if currentHash not in seen:
                seen[currentHash] = [root, False]
            else:
                seen[currentHash][1] = True

            return currentHash

        traverse(root)
        return [candidate[0] for candidate in seen.values() if candidate[1]]
