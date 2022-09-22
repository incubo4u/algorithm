from typing import List


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        rstart, rend = toBeRemoved
        ret = []
        for i, (s, e) in enumerate(intervals):
            if s > rend or e < rstart:
                ret.append((s, e))
                continue
            if s < rstart:
                ret.append((s, rstart))
            if e > rend:
                ret.append((rend, e))
        return ret
