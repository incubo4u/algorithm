from collections import defaultdict
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = defaultdict(int)
        for i, c in enumerate(s):
            if c not in seen:
                seen[c] = i
            elif (i - seen[c]) - 1 != distance[ord(c) - 97]:
                return False
        return True

