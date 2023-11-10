from collections import defaultdict, deque


class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        indeg = defaultdict(list)
        for a, b in adjacentPairs:
            indeg[a].append(b)
            indeg[b].append(a)
        start = min(indeg, key=lambda k: len(indeg[k]))
        seen = set()
        arr = []
        que = deque([start])
        while que:
            curr = que.popleft()
            arr.append(curr)
            seen.add(curr)
            for ngb in indeg[curr]:
                if ngb in seen:
                    continue
                que.append(ngb)
        return arr
