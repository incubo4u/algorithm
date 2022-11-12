from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len(heights) - sum(map(lambda t: int(heights[t[0]] == t[1]), enumerate(sorted(heights)))) 