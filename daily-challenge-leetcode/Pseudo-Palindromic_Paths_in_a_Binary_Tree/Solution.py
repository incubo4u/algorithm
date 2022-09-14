from typing import Optional


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        score = 0
        
        def traverse(root, counter):
            nonlocal score
            if not root:
                return
            counter[root.val]+=1
            if not root.left and not root.right:
                odd = 0
                for freq in counter:
                    if odd > 1: return
                    if freq == 0: continue
                    if freq % 2 == 1: odd += 1
                if odd <= 1:
                    score += 1

            traverse(root.left, counter[::])
            traverse(root.right, counter[::])

        traverse(root, [0 for i in range(10)])
        return score