from collections import defaultdict
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        curr_time = 0
        d = defaultdict(int)
        for task in tasks:
            curr_time += 1
            if d[task] > curr_time:
                wait = d[task] - curr_time
                curr_time += wait
                d[task] = curr_time + space + 1
            else:
                d[task] = curr_time + space + 1

        return curr_time
