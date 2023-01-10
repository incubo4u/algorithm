from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr = intervals[0][1]
        ans = -1
        for start, end in intervals:
            if curr > start:
                curr = min(end, curr)
                ans += 1
            else:
                curr = max(end, curr)
        return ans