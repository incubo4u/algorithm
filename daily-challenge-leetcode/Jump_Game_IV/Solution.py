from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        J = defaultdict(list)
        lenght = len(arr)

        for i, n in enumerate(arr):
            J[n].append(i)

        que = deque([0])
        seen = set()
        best = [inf] * lenght
        best[0] = 0

        while que:

            i = que.popleft()
            d = best[i]

            if i == lenght - 1:
                return d

            for idx in (i - 1, i + 1):
                if 0 <= idx < lenght and best[i] + 1 < best[idx]:
                    best[idx] = best[i] + 1
                    que.append(idx)

            if arr[i] not in seen:
                seen.add(arr[i])

                for idx in J[arr[i]]:
                    best[idx] = min(best[idx], best[i] + 1)
                    que.append(idx)
