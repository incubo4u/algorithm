from typing import List


class Solution:

    def mostPoints(self, q: List[List[int]]) -> int:
        q = q[::-1]
        for i, (earn, jump) in enumerate(q):
            if (j := i - jump - 1) >= 0:
                q[i][0] = earn + q[j][0]
            if i - 1 >= 0:
                q[i][0] = max(q[i - 1][0], q[i][0])
        return q[-1][0]