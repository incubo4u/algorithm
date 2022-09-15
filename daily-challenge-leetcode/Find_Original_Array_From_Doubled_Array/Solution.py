from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ret = []
        smaller = Counter()
        for x in changed:
            if x % 2 == 0 and x // 2 in smaller and smaller[x // 2] > 0:
                smaller[x // 2] -= 1
                ret.append(x // 2)
            else:
                smaller[x] += 1
        if len(ret) * 2 != len(changed):
            return []
        return ret
