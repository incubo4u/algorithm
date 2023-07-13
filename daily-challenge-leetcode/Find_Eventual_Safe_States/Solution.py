from functools import cache


class Solution:

    def eventualSafeNodes(self, g: list[list[int]]) -> list[int]:

        @cache
        def tr(node):
            if node in seen:
                return 0
            seen.add(node)
            for n in g[node]:
                if not tr(n):
                    return 0
            seen.remove(node)
            return 1

        ans = []
        seen = set()
        for n in range(len(g)):
            if tr(n):
                ans.append(n)
        return ans
