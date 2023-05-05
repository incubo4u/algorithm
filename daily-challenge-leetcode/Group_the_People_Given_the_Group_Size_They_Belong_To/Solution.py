from typing import List
from collections import defaultdict


class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        ans = []
        for i, size in enumerate(groupSizes):
            d[size].append(i)
        for k, val in d.items():
            for i in range(0, len(val), k):
                ans.append(val[i:i + k])
        return ans
