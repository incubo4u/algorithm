from typing import List
from collections import defaultdict


class Solution:

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        outdeg = defaultdict(set)
        for a, b in roads:
            outdeg[a].add(b)
            outdeg[b].add(a)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if i == j:
                    continue
                ans = max(
                    ans,
                    len(outdeg[i]) + len(outdeg[j]) - int(i in outdeg[j]))
        return ans
