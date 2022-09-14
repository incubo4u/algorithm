from typing import Optional


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        score = 0

        def traverse(root, counter):
            if not root:
                return

            counter[root.val] = not counter[root.val]
            if not root.left and not root.right:
                if sum(counter) <= 1:
                    nonlocal score
                    score += 1

            traverse(root.left, counter[::])
            traverse(root.right, counter[::])

        traverse(root, [False] * 10)
        return score
