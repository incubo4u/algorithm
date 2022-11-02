from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        que = deque([(start, 0)])
        seen = set()
        while que:
            curr, distance = que.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            if curr == end:
                return distance
            for mutation in bank:
                if len(set(enumerate(mutation)) - set(enumerate(curr))) != 1:
                    continue
                que.append((mutation, distance + 1))
        return -1
