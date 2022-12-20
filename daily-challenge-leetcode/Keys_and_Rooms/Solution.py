from typing import List


class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = {}
        for v, keys in enumerate(rooms):
            g[v] = keys
        seen = set()

        def dfs(v):
            if v in seen:
                return
            seen.add(v)
            for room in g[v]:
                dfs(room)

        dfs(0)
        return len(seen) == len(rooms)
