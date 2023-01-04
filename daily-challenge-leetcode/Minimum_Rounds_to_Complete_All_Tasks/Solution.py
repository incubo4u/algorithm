from functools import cache
from typing import List


class Solution:

    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        n = len(tasks)
        INF = 100000

        @cache
        def complete(i):
            if i > len(tasks) - 1:
                return 0
            if i + 2 < n and tasks[i] == tasks[i + 1] == tasks[i + 2]:
                return min(complete(i + 3), complete(i + 2)) + 1
            if i + 1 < n and tasks[i] == tasks[i + 1]:
                return complete(i + 2) + 1
            return INF

        return ans if (ans := complete(0)) < INF else -1
