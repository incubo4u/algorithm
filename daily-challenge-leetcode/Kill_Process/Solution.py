from typing import List
from collections import defaultdict, deque


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for i, (child, parent) in enumerate(zip(pid, ppid)):
            tree[parent].append(child)
        que = deque()
        que.append(kill)
        ret = [kill]
        while que:
            root = que.popleft()
            ret.extend(tree[root])
            que.extend(tree[root])
        return ret
