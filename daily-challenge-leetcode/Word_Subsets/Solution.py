from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, universal: List[str], subset: List[str]) -> List[str]:
        allSubset = Counter()
        for s in subset:
            allSubset |= Counter(s)
        return [u for u in universal if not allSubset - Counter(u)]

