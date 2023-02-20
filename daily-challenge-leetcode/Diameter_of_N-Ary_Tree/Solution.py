# Definition for a Node.
class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0

        def measure(root):
            if not root or not root.children:
                return 0
            ret = sorted(map(lambda n: measure(n) + 1, root.children))
            nonlocal ans
            if len(ret) > 1:
                ans = max(ans, ret[-1] + ret[-2])
                return ret[-1]
            elif ret:
                ans = max(ans, ret[-1])
                return ret[-1]

        measure(root)
        return ans
