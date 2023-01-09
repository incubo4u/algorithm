from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(reverse=True)
        while intervals:
            ans.append(intervals.pop())
            while intervals and ans[-1][1] >= intervals[-1][0]:
                ans[-1][1] = max(ans[-1] + intervals.pop())
        return ans
