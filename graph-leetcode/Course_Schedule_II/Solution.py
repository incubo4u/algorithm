from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(N))
        prereqs_course, prereqs_amount = defaultdict(list), defaultdict(int)
        for _, (c, pr) in enumerate(prerequisites):
            prereqs_amount[c] += 1
            prereqs_course[pr].append(c)
        ans = []
        que = deque()
        que.extend(set(range(N)) - set(prereqs_amount))
        while que:
            pr = que.popleft()
            ans.append(pr)
            for c in prereqs_course[pr]:
                prereqs_amount[c] -= 1
                if prereqs_amount[c] < 1:
                    que.append(c)
        if len(ans) == N:
            return ans
        return []
