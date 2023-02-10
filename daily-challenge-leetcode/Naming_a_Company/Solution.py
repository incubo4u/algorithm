from typing import List
from collections import defaultdict


class Solution:

    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        ans = 0
        for w in ideas:
            d[w[0]].add(w[1:])
        for k, v in d.items():
            for kk, vv in d.items():
                if k == kk:
                    continue
                ans += ((len(v) -
                         (intersection_lenght := len(v.intersection(vv)))) *
                        ((len(vv)) - intersection_lenght))
        return ans