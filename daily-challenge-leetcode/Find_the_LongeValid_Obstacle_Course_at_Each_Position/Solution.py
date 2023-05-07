import bisect
from math import inf
from typing import List


class Solution:

    def longestObstacleCourseAtEachPosition(self,
                                            obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = []
        heights = [inf] * (n + 1)
        for i, h in enumerate(obstacles):
            j = bisect.bisect(heights, h)
            ans.append(j + 1)
            heights[j] = h

        return ans
