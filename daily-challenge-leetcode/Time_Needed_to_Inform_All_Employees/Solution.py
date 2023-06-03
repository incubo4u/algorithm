from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: list[int],
                     informTime: list[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)

        def dfs(id):
            ret = 0
            for emp in g[id]:
                ret = max(dfs(emp) + informTime[id], ret)
            return ret

        return dfs(headID)
