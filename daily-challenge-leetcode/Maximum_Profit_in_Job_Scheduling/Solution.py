from functools import cache
from typing import List


class Solution:

    def jobScheduling(self, S: List[int], E: List[int], P: List[int]) -> int:
        jobs = tuple(sorted(zip(S, E, P)))
        n = len(jobs)

        @cache
        def get_max(i):
            if i > n - 1:
                return 0
            j = i + 1
            while j < n and jobs[i][1] > jobs[j][0]:
                j += 1
            return max(get_max(j) + jobs[i][2], get_max(i + 1))

        return get_max(0)